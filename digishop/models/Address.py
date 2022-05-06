from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=500)
    active = models.BooleanField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    pincode = models.IntegerField()


