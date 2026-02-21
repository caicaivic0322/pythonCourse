from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_approved = models.BooleanField(default=False, help_text="Designates whether this user has been approved by a teacher.")
    xp = models.IntegerField(default=0, help_text="Experience points for gamification.")
    level = models.IntegerField(default=1, help_text="Current level of the student.")

    def __str__(self):
        return self.username
