from django.shortcuts import render, redirect
from django.contrib.auth import logout
from activity_logs.models import Activity  # Corrected import to refer to the 'activity_logs' app

def dashboard_view(request):
    # Retrieve the 4 most recent logs from the ActivityLog model
    recent_logs = Activity.objects.all().order_by('-timestamp')[:4]
    
    # Pass the logs to the template
    return render(request, 'dashboard.html', {'recent_logs': recent_logs})

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page
