from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    """Страница профиля пользователя"""
    
    return render(request, 'advuser/profile.html')
