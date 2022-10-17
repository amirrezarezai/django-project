from django.db import models

# Create your models here
class Link_model(models.Model):
    address = models.CharField(max_length=300,null=True,blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name