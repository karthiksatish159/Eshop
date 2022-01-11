from django.db import models


class Order12(models.Model):
    objects = None
    product_name = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.IntegerField()