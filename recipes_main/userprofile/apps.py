from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userprofile'

   
    # standartine f-ja
    def ready(self):
        from .signals import create_profile, save_profile
