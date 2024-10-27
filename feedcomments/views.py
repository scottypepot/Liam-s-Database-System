from django.shortcuts import render, redirect
from .models import Feedback
from django.utils import timezone

def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-timestamp')
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})

def add_feedback(request):
    if request.method == 'POST':
        user = request.POST['user']
        comment = request.POST['comment']
        Feedback.objects.create(user=user, comment=comment, timestamp=timezone.now())
        return redirect('feedback_list')
    return render(request, 'add_feedback.html')
