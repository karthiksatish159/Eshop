from django.db import models
from .category import Category

list1=[]

class Product(models.Model):
    object = None
    objects = None
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    related_product_category = models.CharField(max_length=50,default='', null=True, blank=True)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')



    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
    @staticmethod
    def get_id(id):
        Product.objects.get(pk=id)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();

    @staticmethod
    def get_category_id(id):
        for i in Product.objects.all():
            if i.id == id:
                return i.related_product_category
