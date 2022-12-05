from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes_list/', views.RecipeListView.as_view(), name='recipes'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user'),
    path('user_recipes_list/', views.UserRecipesListView.as_view(), name="user_recipes_list"),
]