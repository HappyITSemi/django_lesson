#
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import path, include

from django_lesson import settings


def home(request):
    if request.method == 'GET':
        msg = {'message': 'Hello there'}
        return render(request, 'index.html', msg)


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('accounts/', include('allauth.urls')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
