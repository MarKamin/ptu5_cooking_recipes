from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.models import User



def home(request):
    recipes_count = Recipe.objects.all().count()
    authors_count = User.objects.all().count()

    context = { 'recipes_count': recipes_count,
                'authors_count': authors_count}
    return render(request, 'recipes/home.html', context)