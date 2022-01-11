from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from store.models import Customer, Contact


class Contact1(View):
    def post(self,request):
        postData = request.POST
        email = postData.get('email')
        phone = postData.get('phone')
        subject = postData.get('subject')
        customer = Contact(email=email,  phone=phone,complaint=subject)
        customer.save()
        email = Customer.get_e()
        message = 'Thank you for your complaint soon our agent will contact you'
        send_mail(
            'Subject - Django Email Testing',
            'Hello ' + 'name' + ',\n' + message,
            'sender@example.com',
            [
                email,
            ]
        )
        return redirect('homepage')