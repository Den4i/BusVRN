from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FeedbackForm

from django.core.mail import BadHeaderError
from celery_tasks.tasks import send_feedback_email_task


def feedback_create(request):
    form = FeedbackForm(request.POST or None, request.FILES or None)
    user = request.user
    context = {
        "user": user,
        "form": form,
    }

    return render(request, "feedback/feedback.html", context)


def send_email(request):
    subject = request.POST.get('subject', '')
    feedtext = request.POST.get('feedtext', '')
    from_email = 'dglonassik@gmail.com'

    form = FeedbackForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

    if subject and feedtext and from_email:
        try:
            send_feedback_email_task.delay(subject, feedtext, from_email, ['dglonassik@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
