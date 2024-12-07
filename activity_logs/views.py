from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from django.utils import timezone
from datetime import timedelta, date  # Import `date` here
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages

@login_required
def activity_list(request):
    # Filter activities for all users, segmented by date
    activities = Activity.objects.all()
    today_activities = Activity.objects.filter(timestamp__date=date.today()).order_by('-timestamp')
    yesterday_activities = Activity.objects.filter(timestamp__date=date.today() - timedelta(days=1)).order_by('-timestamp')
    older_activities = Activity.objects.filter(timestamp__date__lt=date.today() - timedelta(days=1)).order_by('-timestamp')

    return render(request, 'activity_list.html', {
        'activities': activities,
        'today_activities': today_activities,
        'yesterday_activities': yesterday_activities,
        'older_activities': older_activities,
    })


@login_required
def add_activity(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        
        # Ensure the message is provided
        if not message:
            # Return an error message to the template if the message is empty
            return render(request, 'add_activity.html', {'error': 'Message cannot be empty.'})

        # The logged-in user will be the one adding the activity
        activity = Activity(user=request.user, message=message)
        activity.save()

        # Optionally, you can also add a success message or redirect to another page
        return redirect('activity_list') 

    return render(request, 'add_activity.html')

@login_required
def update_activity(request, id):
    activity = get_object_or_404(Activity, id=id)

    if request.method == 'POST':
        message = request.POST.get('message')
        activity.message = message
        activity.save()
        return redirect('activity_list')  # Replace with your activity list URL name
    
    return redirect('activity_list')  # Optional fallback

@login_required
def delete_activity(request, id):
    activity = get_object_or_404(Activity, id=id)

    # Admins and users can delete their own activity, admins can delete any activity
    if not (request.user == activity.user or request.user.is_staff):
        messages.error(request, "You are not allowed to delete this activity.")
        return redirect('activity_list')

    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list')

    return render(request, 'delete_activity.html', {'activity': activity})
