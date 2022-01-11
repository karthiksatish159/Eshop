from django.shortcuts import render
from django.views import View

from store.models import Customer, Address


class Edit2(View):
    def post(self,request,id):
        get_data = Address.objects.get(pk=id)
        par = {'address': get_data}
        return render(request,'edit1.html',par)