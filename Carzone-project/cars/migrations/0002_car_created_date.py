# Generated by Django 4.0.4 on 2022-10-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
