from django.db import models
import datetime as dt

# Create your models here.
class   Images(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    # location = models.ForeignKey(Location)
    # category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
