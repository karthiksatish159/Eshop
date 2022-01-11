from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import error
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
class Forgot(View):
    return_url = None
    def post(self, request):
        email = request.POST.get('email')
        email_check = Customer.email_check(email)
        if email_check:
            message = Customer.otpgen()

            send_mail(
                'Subject - SPD2483 Mail Testing',
                'Hello ' + ' Please use this otp to reset your password' + ',\n' + message,
                'sender@example.com',
                [
                    email,
                ]
            )
            return render(request ,'otp_pass.html')
        else:
            return render(request,'forgot_fail.html')