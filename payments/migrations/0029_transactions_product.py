# Generated by Django 3.2 on 2021-05-08 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0028_auto_20210508_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='payments.subsplans'),
            preserve_default=False,
        ),
    ]
