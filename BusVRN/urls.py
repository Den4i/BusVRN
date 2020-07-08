"""BusVRN URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

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
    path('accounts/', include('advuser.urls')),
    path('mappa/', get_map, name='get_mappa'),

    path('', post_list, name='post_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, never_cache(serve), document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
