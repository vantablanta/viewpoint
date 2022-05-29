from re import I
from django.test import TestCase
from .models import Category, Image, Location
from django.contrib.auth.models import User



class ImageTest(TestCase):
    def setUp(self):
        self.new_location = Location(place ='Hungary')
        self.new_location.save_location()
        self.new_category = Category(category='babies')
        self.new_category.save_category()
        self.new_image_owner = User(username='owner')
        self.new_image_owner.save()

        self.new_image = Image(owner= self.new_image_owner, image_name='Nice Image', image_description='Beautiful Description', 
            image_location=self.new_location, image_category=self.new_category
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0 )

    def test_delete_method(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0 )

class CategoryTests(TestCase):
    def setUp(self):
        self.new_category = Category(category='babies')
        self.new_category.save_category()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0 )

    def test_delete_method(self):
        self.new_category.save_category()
        self.new_category.delete_category()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0 )



class LocationTests(TestCase):
    def setUp(self):
        self.new_location = Location(place='Hungary')
        self.new_location.save_location()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0 )

    def test_delete_method(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0 )

