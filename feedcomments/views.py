from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback, Comment
from django.utils.timezone import now, localtime
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.exceptions import PermissionDenied


@login_required
def feedback_list(request):
    today = localtime(now()).date()  # Ensure timezone-aware date
    yesterday = today - timedelta(days=1)

    feedbacks_today = Feedback.objects.filter(timestamp__date=today).order_by('-timestamp')
    feedbacks_yesterday = Feedback.objects.filter(timestamp__date=yesterday).order_by('-timestamp')
    feedbacks_older = Feedback.objects.filter(timestamp__lt=yesterday).order_by('-timestamp')

    # Initialize or retrieve the toggle state from session
    feedback_ids_to_show_comment = request.session.get('feedback_ids_to_show_comment', [])

    # Combine all feedbacks for toggle handling
    all_feedbacks = list(feedbacks_today) + list(feedbacks_yesterday) + list(feedbacks_older)

    # Check for toggle requests
    for feedback in all_feedbacks:
        param_name = f"toggle_comment_{feedback.id}"
        if param_name in request.GET:
            # Add or remove the feedback ID from the list
            if feedback.id in feedback_ids_to_show_comment:
                feedback_ids_to_show_comment.remove(feedback.id)  # Toggle off
            else:
                feedback_ids_to_show_comment.append(feedback.id)  # Toggle on

            # Save updated state in the session
            request.session['feedback_ids_to_show_comment'] = feedback_ids_to_show_comment
            break  # Process only one toggle per request

    return render(request, 'feedback_list.html', {
        'feedbacks_today': feedbacks_today,
        'feedbacks_yesterday': feedbacks_yesterday,
        'feedbacks_older': feedbacks_older,
        'feedback_ids_to_show_comment': feedback_ids_to_show_comment,
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

@login_required
def add_comment(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if request.method == "POST":
        message = request.POST.get('comment')
        if message:
            Comment.objects.create(
                feedback=feedback,
                user=request.user,
                message=message
            )
    return redirect('feedback_list')

@login_required
def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    # Ensure only the owner can edit
    if comment.user != request.user:
        raise PermissionDenied("You are not allowed to edit this comment.")

    if request.method == "POST":
        message = request.POST.get("message")
        if message:
            comment.message = message
            comment.save()
            return redirect('feedback_list')  # Redirect back to the feedback page
    return redirect('feedback_list')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure only the comment's author can delete
    if request.user == comment.user:
        comment.delete()

    return redirect('feedback_list')  # Redirect back to the feedback list