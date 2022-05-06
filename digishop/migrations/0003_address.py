# Generated by Django 3.1.5 on 2021-01-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digishop', '0002_auto_20210102_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('active', models.BooleanField()),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('pincode', models.IntegerField(max_length=6)),
            ],
        ),
    ]
