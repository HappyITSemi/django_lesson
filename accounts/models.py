# Utility = ImageKit
# pip3 install -U django-imagekit
#
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'
        # db_table = 'custom_user'

    # avatar = models.ImageField(upload_to='avatars')  # original
    # avatar_thumbnail = ImageSpecField(source='avatar',
    #                                   processors=[ResizeToFill(100, 50)],
    #                                   format='PNG',
    #                                   options={'quality': 60})


# <ul class="list-unstyled image-list">
#     {% for image in image_list %}
#     <li>
#         <a href="{% url 'image_detail' image.id %}">
#             <img src="{{ image.thumbnail.url }}" width="250">
#         </a>
#     </li>
#     {% endfor %}
# </ul>

