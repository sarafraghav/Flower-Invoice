# Generated by Django 3.2 on 2021-05-06 13:17

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0026_alter_subsplans_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ot_product',
            name='icon',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
