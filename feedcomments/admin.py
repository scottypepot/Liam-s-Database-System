from django.contrib import admin
from .models import Feedback, Comment

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'timestamp')
    search_fields = ('user__username', 'comment')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('feedback', 'user', 'message', 'timestamp')
    search_fields = ('feedback__comment', 'user__username', 'message')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
