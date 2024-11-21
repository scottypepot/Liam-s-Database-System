from django.db import models
from django.conf import settings  # Import settings to use AUTH_USER_MODEL

class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='branches')  # Updated to use AUTH_USER_MODEL

    def __str__(self):
        return self.branch_name
