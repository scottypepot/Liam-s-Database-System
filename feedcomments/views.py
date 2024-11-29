from django.shortcuts import render, redirect
from .models import Feedback
from django.utils import timezone
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-timestamp')
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})

@login_required
def add_feedback(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        feedback = Feedback(user=request.user, comment=comment)
        feedback.save()
        return redirect('feedback_list')

    return render(request, 'add_feedback.html')


def delete_feedback(request, id):
    feedback = get_object_or_404(Feedback, id=id)
    
    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback_list') 

    return render(request, 'delete_feedback_confirm.html', {'feedback': feedback})

def update_feedback(request, id):
    feedback = get_object_or_404(Feedback, id=id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')  # Redirect after successful update
    else:
        form = FeedbackForm(instance=feedback)

    return render(request, 'update_feedback.html', {'form': form, 'feedback': feedback})