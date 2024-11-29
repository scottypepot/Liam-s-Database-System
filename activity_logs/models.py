from django.db import models
from authentication.models import UserProfile  # Importing the UserProfile model

class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return a more meaningful string representation of the activity
        return f'Activity by {self.user.username} on {self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}: {self.message[:20]}...'

