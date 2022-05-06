from django.db import models
from digishop.models import Product
from digishop.models import User


class Payment(models.Model):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    payment_request_id = models.CharField(max_length=200, null=False, unique=True)
    payment_id = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=200, default='Failed')
    created_at = models.DateTimeField(auto_now_add=True)
