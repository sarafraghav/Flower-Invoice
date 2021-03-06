# Generated by Django 3.2 on 2021-05-05 17:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0021_alter_subsplans_trial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsplans',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999)]),
        ),
        migrations.AlterField(
            model_name='subsplans',
            name='trial',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(730)]),
        ),
    ]
