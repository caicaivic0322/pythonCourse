import argparse
import os
from collections import defaultdict

import django
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course, Lesson, UserCourseProgress, UserLessonProgress


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', default='GESP 2级：逻辑进阶')
    parser.add_argument('--keep-id', type=int)
    parser.add_argument('--keep-order', type=int)
    parser.add_argument('--apply', action='store_true')
    return parser.parse_args()


def course_weight(course):
    chapters = list(course.chapters.all())
    lessons = Lesson.objects.filter(chapter__course=course).count()
    quizzes = sum(lesson.quizzes.count() for chapter in chapters for lesson in chapter.lessons.all())
    return (len(chapters), lessons, quizzes, course.id)


def choose_keep_course(courses, keep_id=None, keep_order=None):
    if keep_id is not None:
        for course in courses:
            if course.id == keep_id:
                return course
        raise ValueError(f'未找到要保留的课程 id={keep_id}')

    if keep_order is not None:
        matched = [course for course in courses if course.order == keep_order]
        if not matched:
            raise ValueError(f'未找到要保留的课程 order={keep_order}')
        return sorted(matched, key=course_weight, reverse=True)[0]

    return sorted(courses, key=course_weight, reverse=True)[0]


def build_lesson_map(source_course, target_course):
    target_chapters = {
        (chapter.order, chapter.title): chapter
        for chapter in target_course.chapters.all()
    }
    lesson_map = {}
    for chapter in source_course.chapters.all():
        target_chapter = target_chapters.get((chapter.order, chapter.title))
        if not target_chapter:
            continue
        target_lessons = {
            (lesson.order, lesson.title): lesson
            for lesson in target_chapter.lessons.all()
        }
        for lesson in chapter.lessons.all():
            mapped = target_lessons.get((lesson.order, lesson.title))
            if mapped:
                lesson_map[lesson.id] = mapped
    return lesson_map


def merge_completed_at(existing_value, incoming_value):
    if not existing_value:
        return incoming_value
    if not incoming_value:
        return existing_value
    return max(existing_value, incoming_value)


def merge_user_course_progress(source_course, target_course, lesson_map):
    summary = defaultdict(int)
    progresses = UserCourseProgress.objects.filter(course=source_course).select_related('current_lesson')
    for progress in progresses:
        mapped_lesson = lesson_map.get(progress.current_lesson_id) if progress.current_lesson_id else None
        target_progress, created = UserCourseProgress.objects.get_or_create(
            user=progress.user,
            course=target_course,
            defaults={
                'is_completed': progress.is_completed,
                'completed_at': progress.completed_at,
                'current_lesson': mapped_lesson,
            }
        )
        if not created:
            target_progress.is_completed = target_progress.is_completed or progress.is_completed
            target_progress.completed_at = merge_completed_at(target_progress.completed_at, progress.completed_at)
            if mapped_lesson:
                target_progress.current_lesson = mapped_lesson
            target_progress.save(update_fields=['is_completed', 'completed_at', 'current_lesson'])
        summary['course_progress_merged'] += 1
    return summary


def merge_user_lesson_progress(source_course, lesson_map):
    summary = defaultdict(int)
    old_lessons = list(Lesson.objects.filter(chapter__course=source_course).values_list('id', flat=True))
    progresses = UserLessonProgress.objects.filter(lesson_id__in=old_lessons).select_related('lesson', 'user')
    for progress in progresses:
        mapped_lesson = lesson_map.get(progress.lesson_id)
        if not mapped_lesson:
            summary['lesson_progress_skipped'] += 1
            continue
        target_progress, created = UserLessonProgress.objects.get_or_create(
            user=progress.user,
            lesson=mapped_lesson,
            defaults={
                'is_completed': progress.is_completed,
                'score': progress.score,
                'completed_at': progress.completed_at,
            }
        )
        if not created:
            target_progress.is_completed = target_progress.is_completed or progress.is_completed
            target_progress.score = max(target_progress.score, progress.score)
            target_progress.completed_at = merge_completed_at(target_progress.completed_at, progress.completed_at)
            target_progress.save(update_fields=['is_completed', 'score', 'completed_at'])
        summary['lesson_progress_merged'] += 1
    return summary


def summarize_course(course):
    chapters = list(course.chapters.all())
    lessons = Lesson.objects.filter(chapter__course=course).count()
    return {
        'id': course.id,
        'chapters': len(chapters),
        'lessons': lessons,
        'course_progress': UserCourseProgress.objects.filter(course=course).count(),
        'lesson_progress': UserLessonProgress.objects.filter(lesson__chapter__course=course).count(),
    }


@transaction.atomic
def dedupe(title, apply_changes, keep_id=None, keep_order=None):
    courses = list(Course.objects.filter(title=title).order_by('id'))
    if len(courses) <= 1:
        print(f'未发现重复课程：{title}')
        return

    keep_course = choose_keep_course(courses, keep_id=keep_id, keep_order=keep_order)
    duplicate_courses = [course for course in courses if course.id != keep_course.id]

    print(f'课程标题：{title}')
    print(f'保留课程：{summarize_course(keep_course)}')
    print('待清理课程：')
    for course in duplicate_courses:
        print(f'  {summarize_course(course)}')

    if not apply_changes:
        print('当前为预览模式，添加 --apply 才会真正清理。')
        return

    total_summary = defaultdict(int)
    for course in duplicate_courses:
        lesson_map = build_lesson_map(course, keep_course)
        for key, value in merge_user_course_progress(course, keep_course, lesson_map).items():
            total_summary[key] += value
        for key, value in merge_user_lesson_progress(course, lesson_map).items():
            total_summary[key] += value
        deleted_id = course.id
        course.delete()
        total_summary['courses_deleted'] += 1
        print(f'已删除重复课程 course_id={deleted_id}')

    print('清理完成：')
    for key in sorted(total_summary):
        print(f'  {key}={total_summary[key]}')
    print(f'保留课程现状：{summarize_course(keep_course)}')


if __name__ == '__main__':
    args = parse_args()
    dedupe(args.title, args.apply, keep_id=args.keep_id, keep_order=args.keep_order)
