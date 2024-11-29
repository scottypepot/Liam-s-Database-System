from django.db import models
from django.conf import settings  # Import settings to use AUTH_USER_MODEL
from django.contrib.auth import get_user_model

class Leave(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # Updated to use AUTH_USER_MODEL
    leave_type = models.CharField(max_length=20, choices=[('Vacation', 'Vacation'), ('Sick', 'Sick'), ('Emergency', 'Emergency')])
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - {self.leave_type}"
    

class LeaveRequest(models.Model):
    employee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type} ({self.status})"
