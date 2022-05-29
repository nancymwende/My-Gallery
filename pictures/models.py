from distutils.command.upload import upload
from unicodedata import category
from django.db import models
import datetime as dt

# Create your models here.
class Images(models.Model):
    image = models.ImageField(null=True,blank=True,upload_to = 'pictures/')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    location = models.ForeignKey('Location', on_delete=models.CASCADE,null=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_image(self,name,description):
        self.name = name
        self.description = description
        self.category = category
        self.save()
    @classmethod
    def filter_by_location(cls, location):
        location = Images.objects.filter(location__name=location).all()
        return location
    
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
    
    @classmethod
    def search_by_category(cls,search_term):
        category = cls.objects.filter(category__icontains=search_term)
        return category    
    
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length =30)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()   

    def __str__(self):
        return self.name        
    
class Location(models.Model):
    name = models.CharField(max_length =30)
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name    
