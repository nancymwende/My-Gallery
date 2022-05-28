from unicodedata import name
from django.test import TestCase
from .models import Location, Category

# Create your tests here.

class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(name="Image Location")
        
    def test_location_name(self):

        location = Location.objects.get(name="Image Location")
        self.assertEqual(location.name, "Image Location")    
        
        
        
        
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Image Category")
        
    def test_category_name(self):

        category = Category.objects.get(name="Image Category")
        self.assertEqual(category.name, "Image Category")
        

