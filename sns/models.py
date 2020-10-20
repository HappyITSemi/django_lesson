# マイグレーション
# $ python3 manage.py makemigrations
# $ python3 manage.py migrate
# from imagekit.models import ImageSpecField, ProcessedImageField
# from imagekit.processors import ResizeToFill
#

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from sns_comment.models import SnsComment


class Sns(models.Model):  # sns_mention
    class Meta:
        managed = True
        db_table = 'sns'
        verbose_name_plural = 'sns'

    # user=me
    me = models.ForeignKey(CustomUser, verbose_name='自分・ユーザー', on_delete=models.CASCADE, related_name='sns_me')
    title = models.CharField(verbose_name='タイトル', blank=False, max_length=32)
    description = models.TextField(verbose_name='内容', null=False, blank=False, max_length=128)
    post_image = models.ImageField(
        upload_to='images/', verbose_name='投稿画像',
        validators=[FileExtensionValidator(['png', ])],
        blank=True, null=True)
    comments = models.ForeignKey(SnsComment, verbose_name='コメント', on_delete=models.PROTECT, default=1)
    like_count = models.IntegerField(verbose_name='いいね数', default=0, null=False)
    comment_count = models.IntegerField(verbose_name='コメント数', default=0, null=False)

    created_at = models.DateTimeField(default=timezone.now, verbose_name='登録日時')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='更新日時')

    def __str__(self):
        return self.title + '→' + self.me.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Sns, self).save(*args, **kwargs)


class Friend(models.Model):
    class Meta:
        managed = True
        db_table = 'friend'
        verbose_name = 'フレンド'

    # me user_id 私の
    # friend_id 友達
    me = models.ForeignKey(CustomUser, verbose_name='自分・ユーザー', on_delete=models.CASCADE, related_name='friend_me')
    my_friend = models.ForeignKey(CustomUser, verbose_name='フレンズ', on_delete=models.CASCADE)


class LikeOn(models.Model):
    class Meta:
        managed = True
        db_table = 'favorite'

    sns = models.ManyToManyField(Sns, verbose_name='メンション')
    like_up = models.BooleanField(default=False)


