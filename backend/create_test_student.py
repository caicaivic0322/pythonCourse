import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create a student user that needs approval
username = 'student_demo'
email = 'student@example.com'
password = 'password123'

if not User.objects.filter(username=username).exists():
    user = User.objects.create_user(username=username, email=email, password=password)
    user.is_approved = False  # Explicitly set to False
    user.save()
    print(f"Created student user: {username} (Pending Approval)")
else:
    print(f"User {username} already exists.")
