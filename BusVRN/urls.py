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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from posts.views import like_post

from django.shortcuts import render


def get_map(request):
    return render(request, 'mappa.html')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^Manuals/objects/', include('Manuals.urls')),
    url(r'^posts/', include("posts.urls", namespace='posts')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^like_post/$', like_post, name='like_post'),
    url(r'^feedback/', include("feedback.urls", namespace='feedback')),

    url(r'^mappa/', get_map, name='get_mappa'),



    url(r'^', include("posts.urls", namespace='posts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
