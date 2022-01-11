from django.shortcuts import render
from django.views import View

from store.models import Order


class Pay3(View):
    def post(self,request):
        l=Order.get_v()
        x=l+6.25
        return render(request, 'payment3.html', {'error': x})
