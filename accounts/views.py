from django.shortcuts import render
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import (authenticate,
                                 get_user_model,
                                 login,
                                 logout)
from django.http import HttpResponseRedirect


def login_view(request):
    print(request.user.is_authenticated())
    title = 'Login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
    return HttpResponseRedirect("/")


def register_view(request):
    title = 'Регистрация'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=user.password)
        login(request, new_user)
    context = {
        "form": form,
        "title": title
    }
    return render(request, "accounts/form.html", context)


def logout_view(request):
   return render()


