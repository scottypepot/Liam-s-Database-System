from django.db import models

class Post(models.Model):
    feedback = models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feedback