from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import error
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)

        if not first_name:
            error_message = "First name required"

        elif first_name:
            if len(first_name) < 4:
                error_message = "First name must be 4 characters long"

        if not last_name:
            error_message = "Last name required"

        if last_name:
            if len(last_name) < 4:
                error_message = "Last name must be 4 characters long"

        if not phone:
            error_message = 'Phone Number required'

        if len(phone) < 10:
            error_message = 'Phone Number must be not less than 10 number Long'

        if len(phone) > 10:
            error_message = 'Phone Number must be not more than 10 number Long'

        if len(password) < 6:
            error_message = 'Password must be 6 char long'

        if len(email) < 5:
            error_message = 'Email must be 5 char long'

        if customer.isExists():
            error_message = "Email Address already registred"

        # saving
        if not error_message:
            Customer.set_email1(email)
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            message=Customer.otpgen()
            send_mail(
                'Subject - SPD2483 Mail Testing',
                'Hello ' + first_name + ',\n' + message,
                'sender@example.com',
                [
                    email,
                ]
            )
            return render(request,'otp.html')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)