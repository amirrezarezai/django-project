from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    #
    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    #
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    car_title = models.CharField(max_length=250,blank=True)
    state = models.CharField(choices=state_choice,max_length=255,blank=True)
    city = models.CharField(max_length=255,blank=True)
    color = models.CharField(max_length=255,blank=True)
    model = models.CharField(max_length=255,blank=True)
    condition = models.CharField(max_length=255,blank=True)
    price = models.IntegerField(blank=True)
    description = RichTextField()
    car_photo = models.ImageField(upload_to='car_photo',blank=True)
    car_photo1 = models.ImageField(upload_to='car_photo',blank=True)
    car_photo2 = models.ImageField(upload_to='car_photo',blank=True)
    car_photo3 = models.ImageField(upload_to='car_photo',blank=True)
    car_photo4 = models.ImageField(upload_to='car_photo', blank=True)
    feature = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=255,blank=True)
    engine = models.CharField(max_length=255,blank=True)
    transmission = models.CharField(max_length=255,blank=True)
    interior = models.CharField(max_length=255,blank=True)
    miles = models.IntegerField(blank=True)
    doors = models.CharField(choices=door_choices,max_length=100,blank=True)
    passengers = models.IntegerField(blank=True,default=0)
    vin_no = models.CharField(max_length=255,blank=True)
    millage = models.IntegerField(blank=True,default=0)
    fuel_type = models.CharField(max_length=255,blank=True)
    no_of_owners = models.CharField(max_length=255,blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.car_title

