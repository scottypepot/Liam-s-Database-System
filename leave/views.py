from django.shortcuts import render, redirect
from .models import Leave
from .forms import LeaveForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def leave_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        leave_id = request.POST.get('leave_id')
        leave_request = Leave.objects.get(id=leave_id)
        
        if action == 'approve' and request.user.is_staff:
            leave_request.status = 'Approved'
            leave_request.save()
            return redirect('leave_list')
        elif action == 'decline' and request.user.is_staff:
            leave_request.status = 'Declined'
            leave_request.save()
            return redirect('leave_list')
    
    # Filter leave requests based on user type
    if request.user.is_staff:
        leaves = Leave.objects.all()  # Admin sees all requests
    else:
        leaves = Leave.objects.filter(user=request.user)  # Regular user sees their own requests
    
    leave_details = []
    for leave in leaves:
        num_days = (leave.end_date - leave.start_date).days + 1 
        leave_details.append((leave, num_days))

    return render(request, 'leave/leave_list.html', {'leave_details': leave_details})

# Apply for a leave
@login_required
def apply_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user  # Assign the logged-in user to the leave request
            leave.save()  # Save the leave request to the database
            return redirect('leave_list')  # Redirect to leave list to show the newly created leave request
    else:
        form = LeaveForm()

    return render(request, 'leave/apply_leave.html', {'form': form})

# Admin can approve or decline leave requests
@login_required
@permission_required('leave.change_leave', raise_exception=True)  # Ensure only users with permission can perform this action
def approve_decline_leave(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        leave_id = request.POST.get('leave_id')
        leave_request = Leave.objects.get(id=leave_id)
        
        if action == 'approve':
            leave_request.status = 'Approved'
            leave_request.save()
        elif action == 'decline':
            leave_request.status = 'Declined'
            leave_request.save()
        
        return redirect('leave_list')
    return redirect('leave_list')  # Default redirection if not POST
