from django.conf.urls import url

from . import views

app_name = 'Manuals'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<object_id>[0-9]+)/$', views.detail, name='detail'),
]