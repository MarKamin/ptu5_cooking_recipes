from django import forms
from .models import Recipe, Ingredient, RecipeComment
from django.forms import inlineformset_factory


# class RecipeForm(forms.ModelForm):

#     class Meta:
#         model = Recipe
#         fields = ['name', 'duration', 'calories', 'steps', 'calories', 'servings']

#     ingredients = forms.ModelMultipleChoiceField(
#         queryset=Recipe.objects.filter(ingredients__amount=100),
#         widget=forms.CheckboxSeMulectltiple
#     )

class RecipeCommentForm(forms.ModelForm):
        
       
        class Meta:
            model = RecipeComment
            fields = ('comment', 'recipe', 'writer',)
            widgets = {
                'recipe': forms.HiddenInput(),
                'writer': forms.HiddenInput(),
            }


  

  
