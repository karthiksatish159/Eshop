from django.db.models import Count
from django.shortcuts import render
from django.views import View

from store.models import Order12


class Pie_chart(View):

    def get(self, request):
        labels = []
        data = []

        queryset = Order12.objects.order_by('product_name').values('product_name').annotate(charge_count=Count('product_name'))
        data = list(queryset.values_list('charge_count', flat=True))
        labels = list(queryset.values_list('product_name', flat=True))
        return render(request, 'dashboard_with_pivot.html', {
            'labels': labels,
            'data': data,
        })


