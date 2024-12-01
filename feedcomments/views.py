from django.shortcuts import render, redirect
from .models import Feedback
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import timedelta
from django.contrib.auth.decorators import login_required


def feedback_list(request):
    today = timezone.now().date()  # Get today's date with timezone-aware datetime
    yesterday = today - timedelta(days=1)
    
    # Get feedback for today, yesterday, and older
    feedbacks_today = Feedback.objects.filter(timestamp__date=today).order_by('-timestamp')
    feedbacks_yesterday = Feedback.objects.filter(timestamp__date=yesterday).order_by('-timestamp')
    feedbacks_older = Feedback.objects.filter(timestamp__lt=yesterday).order_by('-timestamp')

    return render(request, 'feedback_list.html', {
        'feedbacks_today': feedbacks_today,
        'feedbacks_yesterday': feedbacks_yesterday,
        'feedbacks_older': feedbacks_older
    })

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