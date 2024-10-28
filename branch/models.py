from django.db import models
from django.contrib.auth.models import User

class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    employees = models.ManyToManyField(User, related_name='branches')

    def __str__(self):
        return self.branch_name
