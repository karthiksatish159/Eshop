from django.db import models
class Address(models.Model):
    objects = None
    email = models.EmailField()
    doorno=models.CharField(max_length=100)
    street_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)



