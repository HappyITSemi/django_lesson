# Generated by Django 3.0.3 on 2020-09-07 14:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200907_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo.Category'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日時'),
        ),
    ]
