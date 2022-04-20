from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image')
    bio = models.CharField(max_length=255, null=True, blank=True)

class Neighborhood(models.Model):
    neighborhoodName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

class Business(models.Model):
    businessName = models.CharField(max_length=100)
    businessPhone = models.CharField(max_length=255, null=True)
    businessEmail = models.EmailField(null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    businessOwner = models.ForeignKey(User, on_delete=models.CASCADE)

class Services(models.Model):
    servicesName = models.CharField(max_length=200)
    servicePhone = models.CharField(max_length=255)
    serviceEmail = models.EmailField(max_length=200)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)