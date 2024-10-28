# views.py
from django.shortcuts import render, redirect
from .models import Leave
from .forms import LeaveForm
from datetime import timedelta

def leave_list(request):
    leaves = Leave.objects.all()
    leave_details = []

    for leave in leaves:
        # Calculate the number of days
        num_days = (leave.end_date - leave.start_date).days + 1  # Add 1 to include the start day
        leave_details.append((leave, num_days))

    return render(request, 'leave/leave_list.html', {'leave_details': leave_details})

def apply_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = None  # Set to None for anonymous submissions
            leave.save()
            return redirect('leave_list')
    else:
        form = LeaveForm()
    return render(request, 'leave/apply_leave.html', {'form': form})
