# Example if Activity has a ForeignKey to another model (e.g., User)
from django.contrib import admin
from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('message',)
    ordering = ('-timestamp',)

admin.site.register(Activity, ActivityAdmin)
