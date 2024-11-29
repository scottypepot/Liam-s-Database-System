from django.contrib import admin
from .models import Branch

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'image')  # Added 'image' for display

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)

        if request.user.role == 'EMPLOYEE':
            perms['change'] = False
            perms['delete'] = False
            perms['add'] = False
        elif request.user.role == 'ADMIN':
            perms['change'] = True
            perms['add'] = True
            perms['delete'] = False  # Admin cannot delete branches
        elif request.user.role == 'SUPERADMIN':
            perms['change'] = True
            perms['add'] = True
            perms['delete'] = True  # Superadmin can delete branches

        return perms

# Register the Branch model with the admin interface
admin.site.register(Branch, BranchAdmin)
