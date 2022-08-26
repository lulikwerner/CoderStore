from django.db import models
from random import randint



class Products(models.Model):
    rand = randint(0, 2000)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    sku = models.IntegerField(default= rand)
    price = models.FloatField()
    stock = models.IntegerField(default= 0)
    image = models.ImageField(upload_to= 'products_image_meats', blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Meats'