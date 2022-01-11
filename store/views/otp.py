import math

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View

from store.models import Customer


class Otp(View):
    def post(self,request):
        otp=request.POST['otp']
        otp1=int(otp)
        if math.floor(math.log10(otp1)+1)==4:
            ootp=Customer.check_otp(otp1)
            if ootp:
                email=Customer.get_email1()
                message='ThankYou for registering,Hope you will enjoy our service'
                send_mail(
                    'Subject - Django Email Testing',
                    'Hello ' + 'name' + ',\n' + message,
                    'sender@example.com',
                    [
                        email,
                    ]
                )
                return render(request,'address.html')
            else:

                return render(request,'otpf.html')
        else:
            id = Customer.get_lastid()
            cu = Customer.objects.get(pk=id)
            cu.delete()
            return render(request,'otpf.html')
