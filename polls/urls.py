from django.urls import re_path

from . import views

app_name = 'polls'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    re_path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]