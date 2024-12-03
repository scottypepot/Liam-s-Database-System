from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from django.utils.timezone import now, localtime
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def feedback_list(request):
    today = localtime(now()).date()  # Ensure timezone-aware date
    yesterday = today - timedelta(days=1)

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
        comment = request.POST.get('message')
        if comment:
            Feedback.objects.create(user=request.user, comment=comment, timestamp=now())
    return redirect('feedback_list')


@login_required
def delete_feedback(request, id):
    feedback = get_object_or_404(Feedback, id=id)

    # Allow users to delete their own feedback and admins to delete any feedback
    if not (request.user == feedback.user or request.user.is_staff):
        messages.error(request, "You are not allowed to delete this feedback.")
        return redirect('feedback_list')

    # Directly delete feedback on POST request
    feedback.delete()
    messages.success(request, "Feedback deleted successfully.")
    return redirect('feedback_list')