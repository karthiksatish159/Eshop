import math

from django.shortcuts import render
from django.views import View
from store.models import Customer
class OTP_PASS(View):
    def post(self,request):
        otp=request.POST['otp']
        otp1=int(otp)
        if math.floor(math.log10(otp1)+1)==4:
            ootp=Customer.check_otp(otp1)
            if ootp:
                return render(request,'forgot1.html')
            else:
                return render(request,'otpf1.html')
        else:
         return render(request,'otpf1.html')
