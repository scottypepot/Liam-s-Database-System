from django.contrib import admin
from .models import LeaveRequest

class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status')
    actions = ['approve_leave']

    def approve_leave(self, request, queryset):
        if request.user.role in ['ADMIN', 'SUPERADMIN']:
            queryset.update(status='Approved')
            self.message_user(request, "Selected leave requests have been approved.")
        else:
            self.message_user(request, "You do not have permission to approve leave requests.")
    
    approve_leave.short_description = "Approve selected leave requests"

# Register the LeaveRequest model with the admin interface
admin.site.register(LeaveRequest, LeaveRequestAdmin)
