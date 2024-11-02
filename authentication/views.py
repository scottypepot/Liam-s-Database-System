from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Redirecting to dashboard...")
            return redirect('dashboard')  # Ensure this matches your URL name for dashboard
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'authentication/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return render(request, 'authentication/register.html')

        # Create a new user account
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')  # Redirect to the login page after registration

    return render(request, 'authentication/register.html')


def forgot_password_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        # Check if the user exists
        user = User.objects.filter(username=username).first()
        
        if user is None:
            messages.error(request, "User not found.")
            return render(request, "authentication/forgot_password.html")
        
        if new_password != confirm_new_password:
            messages.error(request, "New passwords do not match.")
        elif not user.check_password(old_password):
            messages.error(request, "Old password is incorrect.")
        else:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Keep user logged in after password change
            messages.success(request, "Password reset successful.")
            return redirect("login")  # Redirect to the login page after password reset

    return render(request, "authentication/forgot_password.html")

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated
    return render(request, 'authentication/dashboard.html')  # Render dashboard template
