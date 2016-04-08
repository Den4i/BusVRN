from django.shortcuts import render_to_response

# Create your views here.

from .forms import SignUpForm


def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("signups/signup.html")