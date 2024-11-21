from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),  # Dashboard path
    path('logout/', views.logout_view, name='logout'),  # Logout path
     path('edit-profile/', views.edit_profile_view, name='edit_profile'),
]
