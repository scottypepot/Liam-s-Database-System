from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def activity_list(request):
    activities = Activity.objects.all().order_by('-timestamp')
    return render(request, 'activity_list.html', {'activities': activities})

@login_required
def add_activity(request):
    if request.method == 'POST':
        user = request.user
        message = request.POST.get('message')
        activity = Activity(user=user, message=message)
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
