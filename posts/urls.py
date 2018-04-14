from django.urls import re_path

from .views import (post_create, post_delete, post_detail, post_list, post_update)

app_name = 'posts'

urlpatterns = [
    re_path(r'^$', post_list, name='list'),
    re_path(r'^create/$', post_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]