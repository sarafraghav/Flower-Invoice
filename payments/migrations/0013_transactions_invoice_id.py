# Generated by Django 3.2 on 2021-04-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0012_auto_20210429_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='invoice_id',
            field=models.CharField(default='hi', max_length=1000),
            preserve_default=False,
        ),
    ]
