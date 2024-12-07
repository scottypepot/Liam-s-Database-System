from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('add/', views.add_feedback, name='add_feedback'),
    path('feedback/delete/<int:id>/', views.delete_feedback, name='delete_feedback'),
    path('feedback/<int:feedback_id>/comment/', views.add_comment, name='add_comment'),
    path('update_comment/<int:id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
