from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password

from store.models import Order12, category
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print( customer, cart, products)
        rate = 0

        #error_message = None
        for product in products:
            #print(cart.get(str(product.id)))
            #print("THis is an=",product.id)
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product.id)))
            rate = rate + product.price

            x = Product.objects.get(pk=product.id)
            #print(x.price)
            e=x.price
            y=Order12(product_name=x.name,payment_method='Credit_card',shipping_cost='0',unit_price=e)
            order.save()
            y.save()
        error_message = rate
        Order.set_v(rate)
        em=[rate]
        print(em)

        print(type(error_message))
        request.session['cart'] = {}

        return render(request,'payment.html',{'error': em})