from django.db import models

# Create your models here.


class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.DecimalField(max_digits=25,decimal_places=2)
    quantity=models.IntegerField()
    description=models.CharField(max_length=225)
    
