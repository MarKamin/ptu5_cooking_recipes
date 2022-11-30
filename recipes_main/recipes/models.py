from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Ingredient(models.Model):
    ingredient = models.CharField(_('ingredient'), max_length=1000)
    amount = models.DecimalField(_('amount'), decimal_places=1, max_digits=4)
    METRICS = (
        ('mg', _("miligram(s)")),
        ('g', _("gram(s)")),
        ('Kg', _("kilogram(s)")),
        ('ml', _("mililiter(s)")),
        ('L', _("liter(s)")),
        (_('Cup'), _("cup(s)")),
        (_('Tspn'), _("tea spoon(s)")),
        (_('Tblspn'), _("table spoon(s)")),

    )
    
    metrics = models.CharField(_('metrics'), max_length=6, choices=METRICS, default='g')

    def __str__(self) -> str:
        return f'{self.amount}{self.metrics} {self.ingredient}'


class Recipe(models.Model):
    name = models.CharField(_('name'), max_length=100)
    ingredients = models.ManyToManyField(Ingredient, verbose_name=_("Ingredients"))
    steps = models.TextField(_('steps'), max_length=10000)
    duration = models.DecimalField(_('duration(min)'), decimal_places=0, max_digits=4)
    calories = models.DecimalField(_('calories'), decimal_places=1, max_digits=4)
    servings = models.DecimalField(_('servings'), decimal_places=1, max_digits=4)


    def __str__(self) -> str:
        return f'"{self.name}" that requires {self.duration} min to make, has {self.servings} servings and about {self.calories} calories' 


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
        return f"{self.writer} on {self.recipe}, date: {self.created_on}"
    
    class Meta:
        ordering = ('-created_on',)

class Rating(models.Model):
    STARS = (
        ('1', _("Awful")),
        ('2', _("Bad")),
        ('3', _("Normal")),
        ('4', _("Deliciuos")),
        ('5', _("Amazing!")),
    )

    stars = models.CharField(_('stars'), max_length=1, choices=STARS)



   
    


    
