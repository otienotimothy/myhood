from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image')
    bio = models.CharField(max_length=255, null=True, blank=True)
    hood = models.OneToOneField(
        'Neighborhood', on_delete=models.SET_NULL, null=True)

class Neighborhood(models.Model):
    neighborhoodName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    creator = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name='hoodCreator')

class Post(models.Model):
    title = models.CharField(max_length=200)
    postBody = models.TextField()
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, related_name='posts')
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

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