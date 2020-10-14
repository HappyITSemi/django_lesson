#
from django.db import models
from django.db.models import *
from django.utils import timezone

from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='カテゴリー名')

    class Meta:
        managed = True
        verbose_name_plural = 'Category'
        db_table = 'category'

    def __str__(self):
        return self.name


class Todo(models.Model):
    class Meta:
        managed = True
        db_table = 'todo'

    name = models.CharField(verbose_name='タイトル名', blank=False, max_length=32)  # null=DB, blank=Form,
    description = models.CharField(verbose_name='内容', null=False, blank=False, max_length=32)
    due_date = models.DateTimeField(verbose_name='期限', null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='登録日時')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='更新日時')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name='カテゴリー選択')
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.name + ' ' + self.category.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        # me = self.request.user
        return super(Todo, self).save(*args, **kwargs)

