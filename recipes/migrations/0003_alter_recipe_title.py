# Generated by Django 3.2.3 on 2021-06-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(
                max_length=255,
                verbose_name='Название рецепта'),
        ),
    ]