from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from django.utils import timezone
from django.utils.timezone import now, localtime
from datetime import timedelta
from django.contrib.auth.decorators import login_required

@login_required
def activity_list(request):
    today = timezone.now().date()  # Get today's date with timezone-aware datetime
    yesterday = today - timedelta(days=1)
    
    # Get activities for today, yesterday, and older
    today_activities = Activity.objects.filter(timestamp__date=today).order_by('-timestamp')
    yesterday_activities = Activity.objects.filter(timestamp__date=yesterday).order_by('-timestamp')
    older_activities = Activity.objects.filter(timestamp__lt=yesterday).order_by('-timestamp')

    return render(request, 'activity_list.html', {
        'today_activities': today_activities,
        'yesterday_activities': yesterday_activities,
        'older_activities': older_activities
    })
@login_required
def add_activity(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        activity = Activity(user=request.user, message=message)
        activity.save()
        return redirect('activity_list') 

    return render(request, 'add_activity.html')


def update_activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    if request.method == 'POST':
        activity.message = request.POST['message']
        activity.save()
        return redirect('activity_list')
    return render(request, 'update_activity.html', {'activity': activity})

def delete_activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list')
    return render(request, 'delete_activity.html', {'activity': activity})