from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeComment
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from userprofile.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .forms import RecipeCommentForm, RecipeUpdateForm, IngredientEditForm, RecipeAddForm
from django.views.generic.edit import FormMixin
from django.db.models import Prefetch



def home(request):
    recipes_count = Recipe.objects.all().count()
    authors_count = User.objects.prefetch_related(Prefetch('recipes')).count()
    # authors_count = Recipe.objects.filter(author=request.user).count()
    recipe_comments = RecipeComment.objects.all()      
    users_count = User.objects.all().count()
    comments_count = RecipeComment.objects.all().count() 

    context = { 'recipes_count': recipes_count,
                'recipe_comments': recipe_comments,
                'authors_count': authors_count,
                'users_count': users_count,
                'comments_count': comments_count }
    return render(request, 'recipes/home.html', context)

class RecipeListView(ListView):
    model = Recipe
    paginate_by = 5
    template_name = 'recipes/recipes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes_count'] = self.get_queryset().count()
        context['recipe_comments'] = RecipeComment.objects.all() 
        # context['is_it_new'] = RecipeComment.is_comment_fresh()
        recipe_id = self.request.GET.get('recipe_id')
        context['recipes'] = Recipe.objects.all()
        if recipe_id:
            context['recipe'] = get_object_or_404(Recipe, id=recipe_id)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(steps__icontains=search))
        recipe_id = self.request.GET.get('recipe_id')
        if recipe_id:
            queryset = queryset.filter(recipe__id=recipe_id)
        return queryset


class RecipeDetailView(FormMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'   
    form_class = RecipeCommentForm

    def get_success_url(self):
        return reverse('recipe', kwargs={'pk': self.get_object().id})

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            messages.error(self.request, _("Something went wrong"))
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.recipe = self.get_object()
        form.instance.writer = self.request.user
        form.save()
        messages.success(self.request, _('Your review have been posted succesfully!'))
        return super().form_valid(form)

    def get_initial(self):
        return {
            'recipe': self.get_object(),
            'writer': self.request.user,
        }
    

class UserListView(ListView):
    model = User
    paginate_by = 5
    template_name = 'recipes/user_list.html'

class UserDetailView(DetailView):
    model = Profile
    template_name = 'recipes/profile_detail.html' 

class UserRecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    paginate_by = 20
    template_name = 'recipes/user_recipes_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user).order_by('name')
        return queryset 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rcp_count'] = self.get_queryset().count()
        return context


class UserRecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/user_delete_recipe.html'
    success_url = reverse_lazy('recipes')

    def test_func(self):
        recipe_instance = self.get_object()
        return self.request.user == recipe_instance.author

    def form_valid(self, form):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            messages.success(self.request, _('Recipe successfully deleted!'))
        else:
            messages.success(self.request, _('deletion canceled'))
        return super().form_valid(form)

class AddRecipeView(CreateView):
    model = Recipe
    form_class = RecipeAddForm
    # fields = ['name', 'duration', 'calories', 'steps', 'calories', 'servings', 'picture']
    template_name = 'recipes/add_recipe.html'
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, _('Recipe successfully added!'))
        return super().form_valid(form)

 
class AddIngredientView(CreateView):
    model = Ingredient
    # form_class = IngredientForm
    fields = ['ingredient', 'amount', 'metrics','recipe']
    template_name = 'recipes/add_ingredient.html'
    success_url = reverse_lazy('recipes')
    

    def form_valid(self, form):
        form.instance.recipe.author = self.request.user
        messages.success(self.request, _("The ingredient was updated sucessfully!"))
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = "recipes/user_recipe_update.html"
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, _("The recipe was updated sucessfully!"))
        return super().form_valid(form)

    def test_func(self):
        recipe_instance = self.get_object()
        return self.request.user == recipe_instance.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = self.get_object()
        return context

class IngredientsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ingredient
    form_class = IngredientEditForm
    template_name = 'recipes/ingredient_edit_form.html'
    success_url = reverse_lazy('recipes')
    
    def test_func(self):
        ingredient_instance = self.get_object()
        return self.request.user == ingredient_instance.recipe.author

    def form_valid(self, form):
        form.instance.recipe.author = self.request.user
        messages.success(self.request, "Ingredient updated")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient'] = self.get_object()
        return context

class IngredientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ingredient
    template_name = 'recipes/user_ingredient_delete.html'
    success_url = reverse_lazy('recipes')

    def test_func(self):
        ingredient = self.get_object()
        return self.request.user == ingredient.recipe.author

    def form_valid(self, form):
        ingredient = self.get_object()
        if self.request.user == ingredient.recipe.author:
            messages.success(self.request, _('Ingredient deleted'))
        else:
            messages.success(self.request, _('Ingredient deletion canceled'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient'] = self.get_object()
        return context

 

      
    

