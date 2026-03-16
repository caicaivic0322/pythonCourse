from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.html import format_html, format_html_join

from courses.models import Lesson, UserLessonProgress

from .models import User

admin.site.site_header = 'PyMaster Admin'
admin.site.site_title = 'PyMaster Admin'
admin.site.index_title = '后台总览'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_approved', 'level', 'xp', 'progress_snapshot', 'is_staff')
    list_filter = ('is_approved', 'level', 'is_staff')
    readonly_fields = ('progress_snapshot', 'lesson_scores_board')
    fieldsets = UserAdmin.fieldsets + (
        ('Gamification', {'fields': ('is_approved', 'xp', 'level')}),
        ('学习进度', {'fields': ('progress_snapshot', 'lesson_scores_board')}),
    )

    change_list_template = 'admin/users/user/change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'score-matrix/',
                self.admin_site.admin_view(self.score_matrix_view),
                name='users_user_score_matrix',
            ),
        ]
        return custom_urls + urls

    def progress_snapshot(self, obj):
        course_count = obj.course_progress.count()
        lesson_count = obj.lesson_progress.count()
        return f'课程 {course_count} · 小节 {lesson_count}'

    progress_snapshot.short_description = '学习进度'

    def lesson_scores_board(self, obj):
        lesson_progress = list(
            UserLessonProgress.objects
            .filter(user=obj)
            .select_related('lesson', 'lesson__chapter', 'lesson__chapter__course')
            .order_by('lesson__chapter__course__order', 'lesson__chapter__order', 'lesson__order', 'id')
        )
        if not lesson_progress:
            return '暂无学习记录'

        top_ids, bottom_ids = self._ranked_score_ids(lesson_progress)
        rows = []
        for progress in lesson_progress:
            css_class = 'score-neutral'
            if progress.id in top_ids:
                css_class = 'score-top'
            elif progress.id in bottom_ids:
                css_class = 'score-bottom'

            rows.append((
                progress.lesson.chapter.course.title,
                progress.lesson.chapter.title,
                progress.lesson.title,
                css_class,
                progress.score,
                '已完成' if progress.is_completed else '进行中',
            ))

        return format_html(
            '''
            <div class="lesson-score-board">
              <style>
                .lesson-score-board table {{ width: 100%; border-collapse: collapse; margin-top: 8px; }}
                .lesson-score-board th, .lesson-score-board td {{ padding: 8px 10px; border-bottom: 1px solid #e5e7eb; text-align: left; vertical-align: top; }}
                .lesson-score-board th {{ font-weight: 700; }}
                .lesson-score-board .score-pill {{ display: inline-block; min-width: 54px; padding: 4px 10px; border-radius: 999px; font-weight: 700; text-align: center; }}
                .lesson-score-board .score-top {{ background: #dcfce7; color: #166534; }}
                .lesson-score-board .score-bottom {{ background: #fee2e2; color: #b91c1c; }}
                .lesson-score-board .score-neutral {{ background: #e5e7eb; color: #374151; }}
              </style>
              <table>
                <thead>
                  <tr>
                    <th>课程</th>
                    <th>章节</th>
                    <th>小节</th>
                    <th>成绩</th>
                    <th>状态</th>
                  </tr>
                </thead>
                <tbody>{}</tbody>
              </table>
            </div>
            ''',
            format_html_join(
                '',
                '''
                <tr>
                  <td>{}</td>
                  <td>{}</td>
                  <td>{}</td>
                  <td><span class="score-pill {}">{} 分</span></td>
                  <td>{}</td>
                </tr>
                ''',
                rows,
            )
        )

    lesson_scores_board.short_description = '小节成绩明细'

    def _ranked_score_ids(self, lesson_progress):
        top_ranked = sorted(lesson_progress, key=lambda item: (-item.score, item.id))[:3]
        top_ids = {item.id for item in top_ranked}

        bottom_ranked = []
        for item in sorted(lesson_progress, key=lambda item: (item.score, item.id)):
            if item.id in top_ids:
                continue
            bottom_ranked.append(item)
            if len(bottom_ranked) == 3:
                break

        bottom_ids = {item.id for item in bottom_ranked}
        return top_ids, bottom_ids

    def score_matrix_view(self, request):
        students = list(
            User.objects
            .filter(is_staff=False)
            .order_by('username')
        )
        student_count = len(students)

        eligible_lessons = list(
            Lesson.objects
            .annotate(participant_count=Count('userlessonprogress__user', distinct=True))
            .filter(participant_count__gte=self._minimum_participants(student_count))
            .select_related('chapter', 'chapter__course')
            .order_by('chapter__course__order', 'chapter__order', 'order', 'id')
        )

        progress_records = list(
            UserLessonProgress.objects
            .filter(user__in=students, lesson__in=eligible_lessons)
            .select_related('user', 'lesson', 'lesson__chapter', 'lesson__chapter__course')
            .order_by('lesson_id', 'user__username', 'id')
        )
        progress_map = {(item.user_id, item.lesson_id): item for item in progress_records}

        ranked_by_lesson = {}
        for lesson in eligible_lessons:
            lesson_records = [item for item in progress_records if item.lesson_id == lesson.id]
            ranked_by_lesson[lesson.id] = self._ranked_score_ids(lesson_records)

        matrix_rows = []
        for student in students:
            row_scores = []
            for lesson in eligible_lessons:
                progress = progress_map.get((student.id, lesson.id))
                if not progress:
                    row_scores.append({'value': '—', 'css_class': 'matrix-score score-empty'})
                    continue

                top_ids, bottom_ids = ranked_by_lesson[lesson.id]
                css_class = 'matrix-score score-neutral'
                if progress.id in top_ids:
                    css_class = 'matrix-score score-top'
                elif progress.id in bottom_ids:
                    css_class = 'matrix-score score-bottom'

                row_scores.append({'value': progress.score, 'css_class': css_class})

            matrix_rows.append({
                'student': student,
                'scores': row_scores,
            })

        context = {
            **self.admin_site.each_context(request),
            'opts': self.model._meta,
            'title': '成绩总表',
            'subtitle': '仅展示测试参与度达到 75% 及以上的小节',
            'students': students,
            'eligible_lessons': eligible_lessons,
            'matrix_rows': matrix_rows,
        }
        return TemplateResponse(request, 'admin/users/user/score_matrix.html', context)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['score_matrix_url'] = reverse('admin:users_user_score_matrix')
        return super().changelist_view(request, extra_context=extra_context)

    def _minimum_participants(self, student_count):
        if student_count == 0:
            return 1
        return max(1, (student_count * 3 + 3) // 4)
