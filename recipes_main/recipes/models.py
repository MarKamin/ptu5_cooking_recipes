from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.urls import reverse

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
        ('Cup', _("cup(s)")),
        ('Tspn', _("tea spoon(s)")),
        ('Tblspn', _("table spoon(s)")),
        ('Oz', _("Oz")),
        ('whole', _("Whole"))
    )
    
    metrics = models.CharField(_('metrics'), max_length=6, choices=METRICS, default='g')

    def __str__(self) -> str:
        if self.metrics == 'whole':
            return f'{int(self.amount)} {self.metrics} {self.ingredient}'
        else:
            return f'{self.amount} {self.metrics} {self.ingredient}'


class Recipe(models.Model):
    name = models.CharField(_('name'), max_length=100)
    author = models.ForeignKey(User,
        verbose_name=_("author"), 
        on_delete=models.CASCADE, 
        related_name='recipe_author')
    ingredients = models.ManyToManyField(Ingredient, verbose_name=_("ingredients"))
    steps = models.TextField(_('steps'), max_length=10000)
    duration = models.DecimalField(_('duration(min)'), decimal_places=0, max_digits=4)
    calories = models.DecimalField(_('calories'), decimal_places=0, max_digits=4)
    servings = models.DecimalField(_('servings'), decimal_places=0, max_digits=4)
    picture = models.ImageField(_('picture'), upload_to='pictures', blank=True, null=True)
    created_on = models.DateTimeField('created_on', auto_now_add=True)

    def __str__(self) -> str:
        return f'"{self.name}" that requires {self.duration} min to make, has {self.servings} servings and about {self.calories} calories' 

    def show_ingredients(self) -> str:
        return ', '.join(ingredients.ingredient + ' ' +str(ingredients.amount)+' '+str( ingredients.metrics) for ingredients in self.ingredients.all()[:3])
    show_ingredients.short_description = 'ingredient(s)'


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

class Rating(models.Model):
    STARS = (
        ('1', _("(1) Awful")),
        ('2', _("(2) Bad")),
        ('3', _("(3) Normal")),
        ('4', _("(4) Deliciuos")),
        ('5', _("(5) Amazing!")),
    )
    recipe = models.ForeignKey(
        Recipe, 
        verbose_name=_("recipe"), 
        on_delete=models.CASCADE, 
        related_name="star")
    rater = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("rater"), 
        on_delete=models.CASCADE, 
        related_name='recipe_ratings')
    stars = models.CharField(_('stars'), max_length=10, choices=STARS)

    def __str__(self) -> str:
        return f'{self.rater} gave {self.stars} star on "{self.recipe.name}" '

    def get_rcp_name(self):
        return self.recipe.name


   
    


    
