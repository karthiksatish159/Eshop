from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import error
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
class Reset(View):
    return_url = None
    def post(self, request):
        email = request.POST.get('email')
        customer = Customer.get_customer_by_email(email)
        if customer:
            return render(request , 'forgot1.html')
        else:
            return render(request,'fail.html')



