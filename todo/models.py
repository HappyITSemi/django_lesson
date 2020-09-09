import django
from django.db import models
from django.db.models import *
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=24, verbose_name='カテゴリー名')

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

    title = models.CharField(verbose_name='タイトル', blank=False, max_length=32)
    description = models.CharField(verbose_name='内容', blank=True, max_length=32)
    due_date = models.DateTimeField(verbose_name='期限', blank=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='登録日時')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='更新日時')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name='カテゴリー選択')

    def __str__(self):
        return self.title + ' ' + self.category.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Todo, self).save(*args, **kwargs)

