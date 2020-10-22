from django.db import models
from django.utils import timezone

from article.models import Article


class Comment(models.Model):
    class Meta:
        managed = True
        db_table = 'comment'
        verbose_name = 'comment'

    description = models.CharField(verbose_name='コメント文')
    article = models.ForeignKey(Article, verbose_name='投稿', on_delete=models.CASCADE, related_name='comment_article')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='登録日時')

    def __str__(self):
        return self.description[0:20]  # + '→'  # + self.me.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        # self.updated_at = timezone.now()
        return super(Comment, self).save(*args, **kwargs)
