from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):  # Extending Django's built-in User model
    ROLE_CHOICES = [
        ('EMPLOYEE', 'Employee'),
        ('ADMIN', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYEE')  # Add role field

    def __str__(self):
        return f"{self.username} ({self.role})"
