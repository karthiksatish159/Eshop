from django.shortcuts import render
from django.views import View

from store.models import Customer


class Edit(View):
    def post(self,request,id):
        get_data = Customer.objects.filter(id=id)
        par = {'customers': get_data}
        return render(request,'edit.html',par)