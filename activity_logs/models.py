from django.db import models

class Activity(models.Model):
    user = models.CharField(max_length=500)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.message[:20]}'