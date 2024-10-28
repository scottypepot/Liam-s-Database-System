from django.urls import path
from . import views

urlpatterns = [
    path('', views.branch_list, name='branch_list'),
]
