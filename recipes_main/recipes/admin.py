from django.contrib import admin
from .models import Ingredient, Recipe, RecipeComment


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 3
    fields = ('ingredient', 'amount', 'metrics')
    can_delete = True

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'amount', 'metrics', 'recipe_name')


# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('get_rcp_name', 'rater', 'stars')
    

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'duration', 'calories', 'servings',)
    list_filter = ('author', 'duration')
    inlines = (IngredientInline, )

    search_fields = ('author',)
    list_editable = ('duration', 'calories', 'servings',)

# Register your models here.
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeComment)
