from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from store.models import Customer


class Edit1(View):
    print("zxcvbnmmmmmmmmmmmkuytrewqasdfgh")
    def get(self,request,id):
        return render(request,'cart.html')

    def post(self,request,id):
        print("zxcvbnm")
        get_data = Customer.objects.get(id=id)
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        pw1 = Customer.get_edit_password(id)
        em = Customer.get_edit_email(id)
        print("PASSWORD:", pw1)
        get_data.first_name = first_name
        get_data.last_name = last_name
        get_data.phone = phone
        get_data.email = em
        get_data.password = pw1
        get_data.save()
        #print("PHONE:",get_data.phone)
        return redirect('profile')