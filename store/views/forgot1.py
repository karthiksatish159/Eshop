from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import error
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
class Forgot1(View):
    return_url = None
    def post(self, request):
        #email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirmpassword')
        email = Customer.get_email()
        print('Email:-',email)
        customer = Customer.get_customer_by_email(email)

        #Customer.get_phone1()
        #Customer.get_phone2()
        if customer:
            if cpassword==password:
               fname=Customer.get_fname(email)
               lname=Customer.get_lname(email)
               phone=Customer.get_phone(email)
               customer.first_name=fname
               customer.last_name = lname
               customer.phone = phone
               customer.email=email
               customer.password = make_password(password)
               customer.save()
               return render(request , 'login.html')
            else:
                return render(request,'pass_fail.html')
        else:
            return render(request,'fail.html')



