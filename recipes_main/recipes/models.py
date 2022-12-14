from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.urls import reverse
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from tinymce.models import HTMLField

User = get_user_model()

class Recipe(models.Model):
    name = models.CharField(_('name'), max_length=100)
    author = models.ForeignKey(User,
        verbose_name=_("author"), 
        on_delete=models.CASCADE, 
        related_name='recipes')
    steps = HTMLField(_('steps'), max_length=10000)
    duration = models.DecimalField(_('duration(min)'), decimal_places=0, max_digits=4, null=True)
    calories = models.DecimalField(_('calories'), decimal_places=0, max_digits=4, null=True)
    servings = models.DecimalField(_('servings'), decimal_places=0, max_digits=4, null=True)
    picture = models.ImageField(_('picture'), upload_to='pictures', blank=True, null=True)
    created_on = models.DateTimeField('created_on', auto_now_add=True)


    def __str__(self) -> str:
        return f'"{self.name}" that requires {self.duration} min to make, has {self.servings} servings and about {self.calories} calories' 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture:
            picture = Image.open(self.picture.path)
            if picture.width > 500 or picture.height > 500:
                output_size = (400, 400)
                picture.thumbnail(output_size)
                picture.save(self.picture.path)

class Ingredient(models.Model):
    ingredient = models.CharField(_('ingredient'), max_length=1000, null=True, blank=True)
    amount = models.DecimalField(_('amount'), decimal_places=2, max_digits=10, null=True, blank=True)
    METRICS = (
        ('mg.', _("miligram(s)")),
        ('g.', _("gram(s)")),
        ('Kg.', _("kilogram(s)")),
        ('pound', _("pound(s)")),
        ('ml.', _("mililiter(s)")),
        ('L.', _("liter(s)")),
        ('gallon', _("gallon(s)")),
        ('Cup', _("cup(s)")),
        ('Tspn.', _("tea spoon(s)")),
        ('Tblspn.', _("table spoon(s)")),
        ('Oz.', _("Oz")),
        ('whole', _("Whole"))
    )
    
    metrics = models.CharField(_('metrics'), max_length=8, choices=METRICS, default='g')
    recipe = models.ForeignKey(Recipe, 
        verbose_name=_("recipe"), 
        on_delete=models.CASCADE, 
        related_name='ingredients')

    def recipe_name(self):
        return f'{self.recipe.name}'

    def __str__(self):
        if self.metrics == 'whole' or 'Tblspn':
            return f'{self.amount} {self.metrics} {self.ingredient}'
        else:
            return f'{float(self.amount)} {self.metrics} {self.ingredient}'
    
    # def all_ingredients(self):
    

class RecipeComment(models.Model):
    recipe = models.ForeignKey(
        Recipe, 
        verbose_name=_("recipe"), 
        on_delete=models.CASCADE, 
        related_name="comments")
    writer = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("writer"), 
        on_delete=models.CASCADE, 
        related_name='recipe_comments')
    created_on = models.DateTimeField('created_on', auto_now_add=True)
    comment = models.TextField(_('comment'), max_length=1000)

    def __str__(self):
        return f"User: {self.writer} on '{self.recipe.name}', date: {self.created_on}"
    
    class Meta:
        ordering = ('-created_on',)
        
    @property
    def is_comment_fresh():
        return (datetime.now() - timedelta(minutes=3))





   
    


    