# Generated by Django 3.2.3 on 2021-06-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_alter_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Описание'),
        ),
    ]