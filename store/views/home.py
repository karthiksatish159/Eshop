from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import error
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

# Create your views here.

class Index(View):

    def post(self, request):

        remove = request.POST.get('remove')
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print("kkkkkkkk:",request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        products = None
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        #request.session.get('cart').clear()
        # print(products)
        # return render(request, 'orders/order.html')
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        Category.set_cid(categoryID)
        print('C:',categoryID)
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products
        data = {}
        languages = Product.objects.all()
        data['products'] = products
        data['categories'] = categories
        data['languages']=languages
        return render(request, 'index.html', data)

    