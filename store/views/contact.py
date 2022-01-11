from django.shortcuts import render
from django.views import View


class Contact(View):
    def get(self,request):
        return render(request,'contact.html')

    def post(self,request):
        return render(request,'contact.html')