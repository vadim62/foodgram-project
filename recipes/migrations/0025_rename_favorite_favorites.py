# Generated by Django 3.2.3 on 2021-06-17 09:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0024_auto_20210617_1440'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorite',
            new_name='Favorites',
        ),
    ]