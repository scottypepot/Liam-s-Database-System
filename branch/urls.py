from django.urls import path
from . import views

urlpatterns = [
    path('', views.branch_list, name='branch_list'),
    path('add/', views.add_branch, name='add_branch'),
    path('branch/<int:branch_id>/update/', views.update_branch, name='update_branch'),
    path('delete_branch/<int:branch_id>/', views.delete_branch, name='delete_branch'),
]
