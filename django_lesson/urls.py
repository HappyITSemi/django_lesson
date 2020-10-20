#
from django.conf.urls import url
from django.conf.urls.static import static
from django.shortcuts import render
from django.urls import path, include
from django.contrib import admin
from django_lesson import settings


def home(request):
    if request.method == 'GET':
        msg = {'message': 'Hello there'}
        return render(request, 'index.html', msg)
    # loginしていなかったら、login → (/auth/login)へリダイレクトする


urlpatterns = [
                  path('home/', home, name="home"),
                  path('admin/', admin.site.urls),
                  path('todo/', include('todo.urls')),
                  path('accounts/', include('allauth.urls')),
                  path('plot/', include('plot.urls')),
                  path('sns/', include('sns.urls')),
                  path('sns_comment/', include('sns_comment.urls')),
                  path('auth/', include('allauth.urls')),
                  path('', include('accounts.urls')),
                  url(r'^rest-auth/', include('rest_auth.urls')),
                  url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
