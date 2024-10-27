from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your dashboard URL name
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'authentication/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'authentication/register.html')
