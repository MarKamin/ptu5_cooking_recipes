# Generated by Django 4.1.3 on 2022-12-06 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_recipe_ingredients_ingredient_recipe_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipecomment',
            old_name='recipe',
            new_name='recipe4com',
        ),
    ]
