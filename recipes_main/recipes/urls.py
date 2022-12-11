from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('tinymce/', include('tinymce.urls')),
    path('recipes_list/', views.RecipeListView.as_view(), name='recipes'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user'),
    path('user_recipes_list/', views.UserRecipesListView.as_view(), name="user_recipes_list"),
    path('user_delete_recipe/<int:pk>/', views.UserRecipeDeleteView.as_view(), name='user_delete_recipe'),
    path('add_recipe/', views.AddRecipeView.as_view(), name='add_recipe'),
    path('add_ingredient/', views.AddIngredientView.as_view(), name='add_ingredient'),
    path('user_recipe_update/<int:pk>/', views.RecipeUpdateView.as_view(), name='user_recipe_update'),
    path('ingredient_detail/<int:pk>/edit', views.IngredientsUpdateView.as_view(), name='ingredient-edit-form'),
    path('ingredient_delete/<int:pk>/delete', views.IngredientDeleteView.as_view(), name='user_ingredient_delete'),
]

  