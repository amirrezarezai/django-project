# Generated by Django 4.0.4 on 2022-10-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(blank=True, max_length=250)),
                ('state', models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('color', models.CharField(blank=True, max_length=255)),
                ('model', models.CharField(blank=True, max_length=255)),
                ('condition', models.CharField(blank=True, max_length=255)),
                ('price', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('car_photo', models.ImageField(blank=True, upload_to='car_photo')),
                ('car_photo1', models.ImageField(blank=True, upload_to='car_photo')),
                ('car_photo2', models.ImageField(blank=True, upload_to='car_photo')),
                ('car_photo3', models.ImageField(blank=True, upload_to='car_photo')),
                ('car_photo4', models.ImageField(blank=True, upload_to='car_photo')),
                ('feature', models.CharField(blank=True, choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=255)),
                ('body_style', models.CharField(blank=True, max_length=255)),
                ('engine', models.CharField(blank=True, max_length=255)),
                ('transmission', models.CharField(blank=True, max_length=255)),
                ('interior', models.CharField(blank=True, max_length=255)),
                ('miles', models.IntegerField(blank=True)),
                ('doors', models.CharField(blank=True, choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=100)),
                ('passengers', models.IntegerField(blank=True, default=0)),
                ('vin_no', models.CharField(blank=True, max_length=255)),
                ('millage', models.IntegerField(blank=True, default=0)),
                ('fuel_type', models.CharField(blank=True, max_length=255)),
                ('no_of_owners', models.CharField(blank=True, max_length=255)),
                ('is_featured', models.BooleanField(blank=True, max_length=100)),
            ],
        ),
    ]
