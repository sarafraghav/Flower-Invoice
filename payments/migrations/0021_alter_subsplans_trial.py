# Generated by Django 3.2 on 2021-05-05 17:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0020_auto_20210505_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsplans',
            name='trial',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(720)]),
        ),
    ]
