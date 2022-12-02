from .models import Profile
from django import forms


class ProfileTypeForm(forms.ModelForm):
    # choose_your_type = forms.ChoiceField(choices = Profile.TYPES)
    class Meta:
        model = Profile
        fields = ('profile_type',)