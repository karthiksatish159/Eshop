from django.shortcuts import render
from django.views import View

from store.models import Product


class Show(View):
    def post(self,request,id):
        get_data = Product.objects.filter(id=id)
        cid = Product.get_category_id(id)
        print("CATEGORY ID:",cid)
        print(get_data)
        products = Product.objects.filter(related_product_category__icontains=cid)
        data = {}
        data['products1'] = get_data
        data['products'] = products
        #par = {'products': get_data}
        print(data['products'])
        return render(request,"show.html",data)