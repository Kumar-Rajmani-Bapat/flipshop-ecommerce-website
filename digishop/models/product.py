
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=0)
    discount = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploads/files', null=True,blank=True)
    thumbnail = models.ImageField(upload_to='uploads/thumbnail',null=True,blank=True)
    link = models.CharField(null=True,blank=True,max_length=500)
    fileSize = models.CharField(null=True,max_length=500)

    def __str__(self):
        return self.name



class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/images',blank=True)
