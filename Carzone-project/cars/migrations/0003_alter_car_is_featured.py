# Generated by Django 4.0.4 on 2022-10-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
