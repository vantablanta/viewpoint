from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self) :
        return self.category

class Location(models.Model):
    place = models.CharField(max_length=200)

    def __str__(self) :
        return self.place

class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    image_name = models.CharField(max_length=200)
    image_description = models.TextField()
    image_location =  models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    image_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['-uploaded', '-updated']

    def __str__(self) :
        return self.image_name