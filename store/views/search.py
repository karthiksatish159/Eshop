from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from store.models import Product, category
from store.views.cart import Cart


class Search(View):
    def get(self,request):
        query = request.GET.get('query', '')
    def post(self,request):
        search=request.POST['search']
        products=Product.objects.filter(name__icontains=search)
        error_message=None
        data = {}
        if products==0:
            error_message="Sorry there are no products matching with your keyword,Please try with another keyword"
        par={'products':products,'error_message':error_message}
        return render(request,'search.html',par)
