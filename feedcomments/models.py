from django.db import models
from authentication.models import UserProfile
from django.utils import timezone

class Feedback(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='feedbacks')
    comment = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"
