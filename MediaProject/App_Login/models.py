from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,models.CASCADE,related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=250,blank=True)
    dob = models.DateField(null=True,blank=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)


class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')


