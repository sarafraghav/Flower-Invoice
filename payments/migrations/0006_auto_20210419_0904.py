# Generated by Django 3.2 on 2021-04-19 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_auto_20210419_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='stripe_price_id',
            field=models.CharField(default='hi', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='stripe_prod_id',
            field=models.CharField(default='hi', max_length=1000),
            preserve_default=False,
        ),
    ]
