from django.contrib import admin
from .models import Leave

# Define the actions for approving and declining leave requests
def approve_leave(modeladmin, request, queryset):
    queryset.update(status='Approved')

approve_leave.short_description = "Approve selected leave requests"

def decline_leave(modeladmin, request, queryset):
    queryset.update(status='Declined')

decline_leave.short_description = "Decline selected leave requests"

# Register the Leave model with custom admin actions
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'status', 'reason')
    list_filter = ('status', 'user')
    search_fields = ('user__username', 'reason')
    actions = [approve_leave, decline_leave]

# Register the Leave model in the admin site
admin.site.register(Leave, LeaveAdmin)
