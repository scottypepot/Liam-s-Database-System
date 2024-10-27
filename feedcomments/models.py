from django.db import models
from django.utils import timezone

class Feedback(models.Model):
    user = models.CharField(max_length=100)
    comment = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.timestamp}"
