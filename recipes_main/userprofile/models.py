from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from PIL import Image
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    TYPES = (
        ('1', _("Grill lover")),
        ('2', _("Picnic enthusiast")),
        ('3', _("Vegatarian")),
        ('4', _("Meat Lover")),
        ('5', _("Pro Chief")),
        ('6', _("Just an average Chief")),
        ('7', _("Cooker on Holidays")),
        ('8', _("Alcocholic")),
        ('8', _("Candy crusher")),
    )

    user = models.OneToOneField(
    get_user_model(),
    verbose_name='user',
    on_delete=models.CASCADE,
    related_name="profile"
    )
    photo = models.ImageField("photo", upload_to='user_profile/photos', null=True, blank=True)
    profile_type = models.CharField(_('types'), max_length=10, choices=TYPES)

    def __str__(self) -> str:
        return f"{self.user} profile"

    