from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),  # Dashboard path
    path('logout/', views.logout_view, name='logout'),  # Logout path
]
