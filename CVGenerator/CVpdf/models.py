from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    summery = models.TextField()
    degree = models.CharField(max_length=300)
    school = models.CharField(max_length=300)
    university = models.CharField(max_length=300)
    previous_work = models.TextField()
    skills = models.TextField()