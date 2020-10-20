#
# pip3 install django-allauth
# https://django-allauth.readthedocs.io/en/latest/advanced.html#creating-and-populating-user-instances
#

from django.shortcuts import render


def top(request):
    return render(request, 'account/login.html')

