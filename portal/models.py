from django.db import models
from datetime import datetime

# Create your models here.

class Roles(models.Model):
  role_name = models.CharField(max_length=50,null=False,blank=False)

class Clients(models.Model):
  name = models.CharField(default="",max_length=50,null=False,blank=False)
  email = models.EmailField(default="",unique=True)
  password = models.CharField(default="",max_length=50,null=False,blank=False)
  mobile_number = models.CharField(default="",max_length=12,null=False,blank=False)
  country = models.CharField(default="",max_length=50,null=False,blank=False)
  city = models.CharField(default="",max_length=50,null=False,blank=False)
  status = models.CharField(default="",max_length=50,null=False,blank=False)
  role = models.ForeignKey(Roles,on_delete=models.CASCADE,default=None)
  registered_on = models.DateTimeField(default=datetime.now)