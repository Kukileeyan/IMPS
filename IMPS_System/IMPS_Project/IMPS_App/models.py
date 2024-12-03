from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_LEVEL_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
    ]

    username = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django User
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    user_level = models.CharField(max_length=10, choices=USER_LEVEL_CHOICES, default='student')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.student_name} ({self.get_user_level_display()})"
