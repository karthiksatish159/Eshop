from django.shortcuts import render
from django.views import View

from store.models import Address


class Address1(View):
    def get(self,request):
        return render(request,'address.html')
    def post(self,request):
        email=request.POST['email']
        street_name=request.POST['street_name']
        doorno= request.POST['doorno']
        state = request.POST['state']
        city = request.POST['city']
        district = request.POST['district']
        landmark = request.POST['landmark']
        pincode = request.POST['pincode']
        address=Address(email=email,doorno=doorno,street_name=street_name,city=city,district=district,landmark=landmark,state=state,pincode=pincode)
        address.save()
        return render(request,'login.html')
