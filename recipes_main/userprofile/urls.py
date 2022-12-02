from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.profile, name='profiles'),
    path('update_profile/', views.profile, name='update_profile'),
]