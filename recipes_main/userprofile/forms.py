from .models import Profile
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("photo",'profile_type', 'about' )
