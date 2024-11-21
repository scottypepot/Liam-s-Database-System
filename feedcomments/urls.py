from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('add/', views.add_feedback, name='add_feedback'),
    path('feedback/delete/<int:id>/', views.delete_feedback, name='delete_feedback'),
    path('feedback/update/<int:id>/', views.update_feedback, name='update_feedback'),
]
