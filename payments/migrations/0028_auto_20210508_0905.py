# Generated by Django 3.2 on 2021-05-08 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0027_alter_ot_product_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_p',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='invoice_p',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='invoice_s',
            name='address',
            field=models.CharField(max_length=1000),
        ),
    ]
