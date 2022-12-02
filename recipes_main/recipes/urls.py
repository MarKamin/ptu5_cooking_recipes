from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes_list/', views.RecipeListView.as_view(), name='recipes'),
    path('users/', views.home, name='users'),
]