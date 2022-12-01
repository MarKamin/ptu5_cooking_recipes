from django.contrib import admin
from .models import Ingredient, Recipe, RecipeComment, Rating

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'amount', 'metrics')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('get_rcp_name', 'rater', 'stars')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'duration', 'calories', 'servings', 'show_ingredients')
    list_filter = ('author', 'duration')

    search_fields = ('author', 'ingredients__ingredient')
    list_editable = ('duration', 'calories', 'servings',)
    filter_horizontal = ['ingredients']


# Register your models here.
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeComment)
admin.site.register(Rating, RatingAdmin)