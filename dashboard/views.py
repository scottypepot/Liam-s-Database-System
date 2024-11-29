from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from activity_logs.models import Activity  # Corrected import to refer to the 'activity_logs' app

@login_required
def dashboard_view(request):
    try:
        recent_logs = Activity.objects.filter(user=request.user).order_by('-timestamp')[:4]
    except Activity.DoesNotExist:
        recent_logs = []

    return render(request, 'dashboard.html', {
        'recent_logs': recent_logs,
        'user': request.user,
    })


def logout_view(request):
    logout(request)  # Log the user out
    messages.success(request, "You have been logged out successfully.")  # Add success message
    return redirect('login')  # Redirect to the login page

@login_required  # Ensure the user is logged in before accessing the edit profile page
def edit_profile_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user_profile = request.user  # 'request.user' is now an instance of UserProfile
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.email = email
        
        # Remove the profile picture change, just use the default user_icon.png
        # (No need for profile picture handling since it's static)
        user_profile.profile_picture = 'path/to/user_icon.png'  # Set default profile icon
        
        user_profile.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('dashboard')

    user_profile = request.user  # Get the logged-in user's profile
    full_name = f"{user_profile.first_name} {user_profile.last_name}"
    
    return render(request, 'edit_profile.html', {
        'user_profile': user_profile,
        'full_name': full_name,
        'date_joined': user_profile.date_joined.strftime('%B %d, %Y')  # Display formatted date joined
    })