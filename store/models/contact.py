from django.db import models
class Contact(models.Model):
    objects = None
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    complaint = models.CharField(max_length=1500)


