# Generated by Django 3.2.3 on 2021-06-13 11:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20210612_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1)],
                verbose_name='Единицы измерения'),
        ),
    ]