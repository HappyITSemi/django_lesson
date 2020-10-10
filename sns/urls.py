from django.urls import path

from sns import views

app_name = 'sns'
urlpatterns = [
    path('', views.SnsIndexView.as_view(), name='sns_index'),
    ]
