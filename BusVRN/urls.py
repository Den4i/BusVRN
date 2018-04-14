"""BusVRN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
# from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from django.shortcuts import render

from posts.views import like_post, post_list


def get_map(request):
    return render(request, 'mappa.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', include("comments.urls")),
    path('posts/', include("posts.urls")),
    path('accounts/', include('registration.backends.default.urls')),
    path('like_post/', like_post, name='like_post'),
    path('feedback/', include("feedback.urls")),
    path('polls/', include('polls.urls')),

    path('mappa/', get_map, name='get_mappa'),

    path('', post_list, name='post_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
