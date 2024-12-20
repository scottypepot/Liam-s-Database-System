from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Branch
from .forms import BranchForm, BranchUpdateForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect


@login_required
def branch_list(request):
    # Only allow admins to view the branch list
    if not request.user.is_staff:
        return redirect('dashboard')  # Redirect to dashboard if not admin
    
    # Fetch all branches and order them by ID in descending order (newest first)
    branches = Branch.objects.all().order_by('-id')  # Ordering by ID to display the newest first
    return render(request, 'branch/branch_list.html', {'branches': branches})

@login_required
def add_branch(request):
    # Only allow admins to add branches
    if not request.user.is_staff:
        return redirect('dashboard')  # Redirect to dashboard if not admin
    
    if request.method == 'POST':
        form = BranchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new branch
            return redirect('branch_list')  # Redirect to the branch list page
    else:
        form = BranchForm()  # Show an empty form if GET request
    
    return render(request, 'branch/add_branch.html', {'form': form})

def add_branch(request):
    if request.method == 'POST':
        # The form now only includes location and image
        form = BranchForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the name to 'Liams' before saving
            branch = form.save(commit=False)  # Don't save yet
            branch.name = 'Liams Flavoured Chicken Wings'  # Set fixed name
            branch.save()  # Now save the branch with the location and image
            return redirect('branch_list')  # Redirect after successful form submission
    else:
        form = BranchForm()

    return render(request, 'branch/add_branch.html', {'form': form})

# Ensure only staff/admins can access this view
@user_passes_test(lambda u: u.is_staff)
def update_branch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    
    if request.method == 'POST':
        # Handle the 'Clear' checkbox for the image
        if 'image-clear' in request.POST:
            branch.image.delete()  # Delete the current image
            branch.image = None  # Reset the image field

        # Update the fields
        branch.name = request.POST.get('name')
        branch.location = request.POST.get('location')
        if 'image' in request.FILES:
            branch.image = request.FILES['image']
        branch.save()
        
        return redirect('branch_list')
    
    return render(request, 'branch/update_branch.html', {'branch': branch})

@login_required
def delete_branch(request, branch_id):
    if request.user.is_staff:
        branch = get_object_or_404(Branch, id=branch_id)
        branch.delete()
        return redirect('branch_list')  # Redirect to the branch list after deletion
    else:
        return redirect('branch_list')  # Or show a forbidden message if the user isn't an admin