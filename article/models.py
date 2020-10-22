# マイグレーション
# $ python3 manage.py makemigrations
# $ python3 manage.py migrate
# from imagekit.models import ImageSpecField, ProcessedImageField
# from imagekit.processors import ResizeToFill
#
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

from accounts.models import CustomUser


class Article(models.Model):
    class Meta:
        managed = True
        db_table = 'article'
        verbose_name_plural = 'article'

    title = models.CharField()
    description = models.TextField()
    post_image = models.ImageField(
        upload_to='image/avatar/', verbose_name='アバター',
        validators=[FileExtensionValidator(['png', ])],
        blank=True, null=True)
    me = models.ForeignKey(CustomUser, verbose_name='私', on_delete=models.CASCADE, related_name='article_me')
    likes = models.IntegerField(verbose_name='いいね数')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='登録日時')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='更新日時')

    def __str__(self):
        return self.title + '→' + self.me.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        # me = self.request.
        return super(Article, self).save(*args, **kwargs)
