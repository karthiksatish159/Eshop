from django.shortcuts import render
from django.shortcuts import render
from django.views import View

from store.models import Customer, Address


class Profile(View):
    def get(self,request):
        email = Customer.get_profile_email()
        first_name = Customer.get_fname(email)
        last_name = Customer.get_lname(email)
        print("qwertyui:",email)

        id = Customer.get_profile_id(email)
        customers=Customer.objects.filter(email__icontains=email)
        #customers = Customer.objects.filter(first_name__icontains=first_name)
        #print("kk:",customers.email)
        #customers = {"first_name":first_name,"last_name":last_name,"email":email}
        print(customers)
        z=Customer.get_email123()
        address=Address.objects.filter(email__icontains=z)
        data = {}
        data['customers'] = customers
        data['address'] = address
        par = {'customers': customers}
        return render(request , 'profile.html',data)