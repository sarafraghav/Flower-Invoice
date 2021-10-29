# Generated by Django 3.2 on 2021-04-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20210419_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='stripe_id',
            field=models.CharField(default='hi', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='stripe_sub_id',
            field=models.CharField(default='hi', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='stripe_session_id',
            field=models.CharField(default='hi', max_length=1000),
            preserve_default=False,
        ),
    ]
