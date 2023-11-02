from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bike(models.Model):
    vechile_name=models.CharField(max_length=200)
    maker=models.CharField(max_length=100)
    cc=models.IntegerField()
    yearofproduction=models.IntegerField()
    rating=models.IntegerField()
    rate_per_Hr=models.IntegerField()
    image_url = models.CharField(max_length=2083)
    seating_capacity=models.IntegerField()
    fuel_type=models.CharField(max_length=20)
    vechilecatagory=models.CharField(max_length=50,default='')
    available=models.BooleanField(default=False)
    
class car(models.Model):
    vechile_name=models.CharField(max_length=200)
    maker=models.CharField(max_length=100)
    cc=models.IntegerField()
    yearofproduction=models.IntegerField()
    rating=models.IntegerField()
    rate_per_Hr=models.IntegerField()
    image_url = models.CharField(max_length=2083)
    seatingcapacity=models.IntegerField()
    fueltype=models.CharField(max_length=20)
    vechilecatagory=models.CharField(max_length=50,default='')
    available=models.BooleanField(default=False)
    
class contact(models.Model):
    name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    

