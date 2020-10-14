# Utility = ImageKit
# pip3 install -U django-imagekit
#
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'
        # db_table = 'custom_user'
