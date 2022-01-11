from django.shortcuts import redirect, render
from django.views import View

from store.models import Product, Category


class Filter(View):
    def post(self,request):

        price=request.POST['filter']
        x=Category.get_cid()
        if x=='email':
            html_project_list = Product.objects.filter(price__lte=price).order_by( '-price').reverse()
            par = {'products': html_project_list}
            return render(request, 'filter.html', par)

        Category.print1()
        html_project_list = Product.objects.filter(related_product_category__icontains=x,price__lt=price).order_by('-price').reverse()
        par = {'products': html_project_list}
        return render(request,'filter.html',par)

