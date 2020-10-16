#
# pip3 install django-allauth

from django.shortcuts import render


def top(request):
    return render(request, 'account/login.html')
