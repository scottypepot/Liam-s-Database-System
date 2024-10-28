from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('add/', views.add_activity, name='add_activity'),
    path('update/<int:id>/', views.update_activity, name='update_activity'),
    path('delete/<int:id>/', views.delete_activity, name='delete_activity'),
]
