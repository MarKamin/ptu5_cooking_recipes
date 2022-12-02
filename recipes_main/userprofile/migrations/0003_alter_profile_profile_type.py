# Generated by Django 4.1.3 on 2022-12-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_profile_profile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('1', 'Grill lover'), ('2', 'Picnic enthusiast'), ('3', 'Vegatarian'), ('4', 'Meat Lover'), ('5', 'Pro Chief'), ('6', 'Just an average Chief'), ('7', 'Cooker on Holidays'), ('8', 'Alcocholic'), ('8', 'Candy crusher')], max_length=10, verbose_name='types'),
        ),
    ]
