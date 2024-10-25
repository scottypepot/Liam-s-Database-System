from django.shortcuts import render, redirect
from .models import Activity
from django.utils import timezone

def activity_list(request):
    activities = Activity.objects.all().order_by('-timestamp')
    return render(request, 'activity_list.html', {'activities': activities})

def add_activity(request):
    if request.method == 'POST':
        user = request.POST['user']
        message = request.POST['message']
        Activity.objects.create(user=user, message=message, timestamp=timezone.now())
        return redirect('activity_list')
    return render(request, 'add_activity.html')
