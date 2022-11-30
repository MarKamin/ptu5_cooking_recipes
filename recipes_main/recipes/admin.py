from django.contrib import admin
from .models import Ingredient, Recipe, RecipeComment, Rating

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeComment)
admin.site.register(Rating)