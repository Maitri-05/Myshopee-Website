from django.db import models
from portal.models import Clients

# Create your models here.
class Category(models.Model):
  category_name=models.CharField(max_length=50,null=False,blank=False)
  category_thumbnail=models.CharField(max_length=100,null=False,blank=False,default=None)
  # added_by=models.ForeignKey(Clients,on_delete=models.SET_DEFAULT,default=None)
  

class Product(models.Model):
  product_name = models.CharField(max_length=50,null=False,blank=False)
  product_price = models.IntegerField(null=False,blank=False)
  product_description = models.CharField(max_length=200,null=False,blank=False)
  product_thumbnail = models.CharField(max_length=100,null=False,blank=False)
  min_order_quantity = models.IntegerField(null=False,blank=False)
  # status = models.CharField(max_length=50,null=False,blank=False,default="")
  
