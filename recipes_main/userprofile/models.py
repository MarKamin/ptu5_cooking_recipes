from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from PIL import Image
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    TYPES = (
        ('Grill lover', _("Grill lover")),
        ("Picnic enthusiast", _("Picnic enthusiast")),
        ("Vegatarian", _("Vegatarian")),
        ('Meat Lover', _("Meat Lover")),
        ('Pro Chief', _("Pro Chief")),
        ('Just an average Chief', _("Just an average Chief")),
        ('Cooker on Holidays', _("Cooker on Holidays")),
        ('Alcocholic', _("Alcocholic")),
        ('Candy crusher', _("Candy crusher")),
    )

    user = models.OneToOneField(
    get_user_model(),
    verbose_name='user',
    on_delete=models.CASCADE,
    related_name="profile"
    )
    photo = models.ImageField("photo", upload_to='user_profile/photos', null=True, blank=True)
    profile_type = models.CharField(_('Choose your type'), max_length=22, choices=TYPES, null=True, blank=True)
    about = models.TextField( _("about"), max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user} {self.profile_type}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            photo = Image.open(self.photo.path)
            if photo.width > 500 or photo.height > 500:
                output_size = (200, 200)
                photo.thumbnail(output_size)
                photo.save(self.photo.path)

    