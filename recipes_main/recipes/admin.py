from django.contrib import admin
from .models import Ingredient, Recipe, RecipeComment, Rating

# class BookInstanceAdmin(admin.ModelAdmin):
#     list_display = ('unique_id', 'book', 'status', 'due_back', 'reader' )
#     list_filter = ('status', 'due_back')
#     readonly_fields = ('unique_id', 'is_overdue')
#     # foreign key __ laukas (apacioj) DJANGI look-ups
#     search_fields = ('unique_id', 'book__title', 'book__author__last_name__exact', 'reader__last_name')
#     # dajngo select2 admin filters
#     list_editable = ('status', 'due_back', 'reader')

#     fieldsets = (
#                 ('General', {'fields': ('unique_id', 'book')}),
#                 ('Availability', {'fields': (('status', 'due_back'), 'reader', 'is_overdue')}),
    # )

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'duration', 'calories', 'servings')
    list_filter = ('author', 'duration')

    search_fields = ('author', 'ingredients__ingredient')
    list_editable = ('duration', 'calories', 'servings')

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeComment)
admin.site.register(Rating)