# Generated by Django 3.1.5 on 2021-01-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digishop', '0003_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
