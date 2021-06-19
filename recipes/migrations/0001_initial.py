# Generated by Django 3.2.3 on 2021-06-03 13:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('unit', models.CharField(max_length=64,
                                          verbose_name='Единицы измерения')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('ingredient',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='recipes.ingredient',
                                   verbose_name='Ингредиент')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(default='', max_length=255, unique=True)),
                ('description', models.TextField(
                    max_length=1000, verbose_name='Описание')),
                ('cooking_time', models.IntegerField(
                    verbose_name='Время приготовления(мин)')),
                ('image', models.ImageField(
                    upload_to='./media/', verbose_name='Картинка')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Автор')),
                ('ingredients', models.ManyToManyField(
                    through='recipes.IngredientRecipe', to='recipes.Ingredient')),
                ('tag', models.ManyToManyField(max_length=64, to='recipes.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='ingredientrecipe',
            name='recipe',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='recipes.recipe',
                verbose_name='Рецепт'),
        ),
    ]