from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_approved', 'level', 'xp', 'is_staff')
    list_filter = ('is_approved', 'level', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Gamification', {'fields': ('is_approved', 'xp', 'level')}),
    )
