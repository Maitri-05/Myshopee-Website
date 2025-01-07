from django.db import models
from datetime import datetime

# Create your models here.
# class Country(models.Model):
#     country_name = models.CharField(max_length=50,null=False,blank=False)
#     country_code = models.CharField(max_length=5,null=False,blank=False)

# class City(models.Model):
#     city_name = models.CharField(max_length=50,null=False,blank=False)
#     country = models.ForeignKey(Country,on_delete=models.CASCADE,default=None)

class Users(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    phone = models.CharField(max_length=12,null=False,blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=50,null=False,blank=False)
    address = models.CharField(max_length=200,null=False,blank=False)
    country = models.CharField(default="",max_length=50,null=False,blank=False)
    city = models.CharField(default="",max_length=50,null=False,blank=False)
    status = models.CharField(max_length=50,null=False,blank=False)
    added_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(blank=True,null=True,default=None)




