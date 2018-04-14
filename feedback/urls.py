from django.urls import re_path

from .views import feedback_create, send_email

app_name = 'feedback'

urlpatterns = [
    re_path('create/', feedback_create, name='feedback_create'),
    re_path('sending/', send_email, name='send_email')
]
