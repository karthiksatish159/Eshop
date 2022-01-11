from django.shortcuts import render, redirect
from django.views import View
class Payment(View):
    def get(self,request):
        return redirect('orders')
    def post(self,request):
        return render(request,'cart.html')
