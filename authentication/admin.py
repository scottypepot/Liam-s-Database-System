from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('role', 'is_active', 'is_staff', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add custom action to deactivate users
    actions = ['deactivate_users']

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected users have been deactivated.")
    
    deactivate_users.short_description = "Deactivate selected users"

    # Restrict admin views based on user role
    def get_model_perms(self, request):
        perms = super().get_model_perms(request)

        # Permissions for Employee (view only)
        if request.user.role == 'EMPLOYEE':
            perms['change'] = False
            perms['delete'] = False
            perms['add'] = False

        # Permissions for Admin (Assistant Manager)
        elif request.user.role == 'ADMIN':
            # Admin can add users, change details but cannot delete or deactivate users
            perms['add'] = True
            perms['change'] = True
            perms['delete'] = False
            perms['deactivate'] = False

        # Permissions for Superadmin (Senior Manager)
        elif request.user.role == 'SUPERADMIN':
            # Superadmins can add, change, delete and deactivate users
            perms['add'] = True
            perms['change'] = True
            perms['delete'] = True
            perms['deactivate'] = True

        return perms

# Register the custom UserProfile admin
admin.site.register(UserProfile, CustomUserAdmin)
