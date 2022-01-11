from django.shortcuts import render
from django.views import View

from store.models import Order


class Pay2(View):
    def post(self,request):
        l=Order.get_v()
        x=l+1.5
        return render(request, 'payment2.html', {'error': x})
