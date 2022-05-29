from django.test import TestCase

from photoapp.views import categories
from .models import Category, Image, Location
from django.contrib.auth.models import User

# Create your tests here.
class ModelTests(TestCase):
    # setup
    def setUp(self):
        self.new_location = Location(place ='Hungary')
        self.new_category = Category(category='babies')
        self.new_image_owner = User(username='owner')
        self.new_image_owner.save()
        self.new_image = Image(owner= self.new_image_owner, image_name='Nice Image', image_description='Beautiful Description', 
            image_location=self.new_location, image_category=self.new_category
        )

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.new_location, Location))
    #     self.assertTrue(isinstance(self.new_category,Category))
    #     self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0 )

        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0 )


        self.new_image.save_image()
        self.new_image_owner = User(username='owner')
        images = Image.objects.all()
        self.assertTrue(len(images) > 0 )