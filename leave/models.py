from django.db import models
from django.contrib.auth.models import User

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow null and blank
    leave_type = models.CharField(max_length=20, choices=[('Vacation', 'Vacation'), ('Sick', 'Sick'), ('Emergency', 'Emergency')])
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - {self.leave_type}"
