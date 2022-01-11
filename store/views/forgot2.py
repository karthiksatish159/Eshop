from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import error
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
class Forgot2(View):
    return_url = None
    def post(self, request):
        return render(request,'forgot.html')