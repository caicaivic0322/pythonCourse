import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course, Chapter, Lesson

# Create Course
course, created = Course.objects.get_or_create(
    title="Python Basics: Launchpad",
    description="Your first step into the world of Python programming.",
    defaults={'order': 1}
)

if created:
    print(f"Created Course: {course.title}")

# Chapter 1
ch1, _ = Chapter.objects.get_or_create(course=course, title="Mission Briefing: Introduction", defaults={'order': 1})
Lesson.objects.get_or_create(
    chapter=ch1, 
    title="What is Python?", 
    defaults={
        'content': "Python is a powerful programming language used for web development, data science, AI, and more.",
        'lesson_type': 'text',
        'order': 1
    }
)
Lesson.objects.get_or_create(
    chapter=ch1, 
    title="Your First Script", 
    defaults={
        'content': "Write `print('Hello World')` to see magic happen.",
        'lesson_type': 'code',
        'order': 2
    }
)

# Chapter 2
ch2, _ = Chapter.objects.get_or_create(course=course, title="Data Storage: Variables", defaults={'order': 2})
Lesson.objects.get_or_create(
    chapter=ch2, 
    title="Variables & Types", 
    defaults={
        'content': "Variables are like boxes where you store data.",
        'lesson_type': 'text',
        'order': 1
    }
)

print("Database seeded successfully!")
