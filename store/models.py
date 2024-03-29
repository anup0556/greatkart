from django.db import models
from category.models import category

class product(models.Model):
  product_name   = models.CharField(max_length=200,unique=True)
  slug           = models.SlugField(max_length=200,unique=True)
  description    = models.TextField(max_length=500,blank=True)
  price          = models.IntegerField()
  image          = models.ImageField(upload_to='photos/products')
  stok           = models.IntegerField()
  is_available   = models.BooleanField(default=True)
  category       = models.ForeignKey(category,on_delete=models.CASCADE)
  created_date   = models.DateTimeField(auto_now_add=True)
  modifield_date = models.DateTimeField(auto_now= True)
  
  def __str__(self):
      return self.product_name


