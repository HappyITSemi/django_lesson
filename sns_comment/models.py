from django.db import models


# Create your models here.

class SnsComment(models.Model):
    class Meta:
        managed = True
        db_table = 'sns_comment'
