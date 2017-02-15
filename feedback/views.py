from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import FeedbackForm

from django.core.mail import send_mail, BadHeaderError


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
    if subject and feedtext and from_email:
        try:
            send_mail(subject, feedtext, from_email, ['dglonassik@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
