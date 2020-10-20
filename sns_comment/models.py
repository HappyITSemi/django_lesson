# SNS Comment

from django.db import models
from django.utils import timezone

from accounts.models import CustomUser


class SnsComment(models.Model):
    class Meta:
        managed = True
        db_table = 'sns_comment'

    # 投稿_id >> sns = sns mention_id - sns_comment
    # sns = models.ForeignKey(Sns, verbose_name='mention', on_delete=models.PROTECT)
    # mention(sns)へ投稿する投稿者ID　=login_user
    me = models.ForeignKey(CustomUser, verbose_name='コメント者', on_delete=models.PROTECT, default=1)
    comment = models.TextField(verbose_name='コメント', blank=False, max_length=128)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='登録日時')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='更新日時')

    def __str__(self):
        return self.comment + '<< ' + self.me.pk

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        # me = login_user_id
        # self.me = self.request.user
        return super(SnsComment, self).save(*args, **kwargs)

