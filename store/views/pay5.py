from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic.base import View

from store.models import Customer


class Pay5(View):
    def post(self,request):
        message = "Your Payment is Confirmed Order will be arrived soon"
        email = Customer.get_e()
        send_mail(
            'Subject - SPD2483 Mail Testing',
            'Hello ' + 'Sir/Mam' + ',\n' + message,
            'sender@example.com',
            [
                email,
            ]
        )
        return render(request,'decision.html')