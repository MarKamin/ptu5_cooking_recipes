from django import forms
from .models import Recipe, Ingredient, RecipeComment
from django.forms import inlineformset_factory


class RecipeCommentForm(forms.ModelForm):
        
        class Meta:
            model = RecipeComment
            fields = ('comment', 'recipe', 'writer',)
            widgets = {
                'recipe': forms.HiddenInput(),
                'writer': forms.HiddenInput(),
            }

class RecipeUpdateForm(forms.ModelForm):

     class Meta:
            model = Recipe
            fields = ('name', 'steps', 'duration', 'calories', 'servings', 'picture')
            widgets = {
                'recipe': forms.HiddenInput(),
                'writer': forms.HiddenInput(),
            }


class IngredientEditForm(forms.ModelForm):
    
    class Meta:
        model = Ingredient
        fields = ( 'ingredient', 'amount', 'metrics', 'recipe')

  

  
