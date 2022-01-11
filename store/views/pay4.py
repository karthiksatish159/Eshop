from django.shortcuts import render
from django.views import View

from store.models import Order


class Pay4(View):
    def post(self,request):
        l=Order.get_v()
        x=l+12.5
        return render(request, 'payment4.html', {'error': x})
