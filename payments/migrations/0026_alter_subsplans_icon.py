# Generated by Django 3.2 on 2021-05-06 04:42

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0025_alter_ot_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsplans',
            name='icon',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
