from unicodedata import category
from django.db import models
import datetime as dt

# Create your models here.
class   Images(models.Model):
    image = models.ImageField
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
