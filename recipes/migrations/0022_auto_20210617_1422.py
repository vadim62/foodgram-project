# Generated by Django 3.2.3 on 2021-06-17 09:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0021_auto_20210617_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='author',
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='user',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='user_sl',
                to='auth.user',
                verbose_name='Подписчик'),
            preserve_default=False,
        ),
    ]