from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404  
from django.contrib.auth import get_user_model
from django.db.models import Count



def home(request):
    recipes_count = Recipe.objects.all().count()
    # authors_count = Recipe.objects.filter(author=1).first().count()
    # authors_count = Recipe.objects.annotate(recipes_count=Count('name'))
    for rcp in Recipe.objects.annotate(recipes_count=Count('name')):
        print(rcp.recipes_count)
        

    context = { 'recipes_count': recipes_count,
                'rcp_count': recipes_count}
    return render(request, 'recipes/home.html', context)

class RecipeListView(ListView):
    model = Recipe
    paginate_by = 1
    template_name = 'recipes/recipes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes_count'] = self.get_queryset().count()
        recipe_id = self.request.GET.get('recipe_id')
        context['authors'] = User.objects.all()
        if recipe_id:
            context['recipe'] = get_object_or_404(User, id=recipe_id)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(author__icontains=query))
        return queryset
