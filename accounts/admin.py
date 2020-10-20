from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    """
    user admin の定義
    see: https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
    """
    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(CustomUser)
