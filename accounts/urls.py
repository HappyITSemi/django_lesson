from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.top, name='account_login'),
 ]

