from django.conf.urls import url

from .views import feedback_create, send_email

app_name = 'feedback'

urlpatterns = [
	url(r'^create/$', feedback_create, name='feedback_create'),
	url(r'^sending/$', send_email, name='send_email')
]