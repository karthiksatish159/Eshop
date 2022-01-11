from django.db import models
import random as r
l = []
l2=[]
l1=[]
l3=[]
l4=[]
l5=[]
l6=[]
class Customer(models.Model):
    objects = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)



    def register(self):
        self.save()

    @staticmethod
    def get_edit_password(id):
        for i in Customer.objects.all():
            if i.id == id:
                return i.password

    def get_edit_email(id):
        for i in Customer.objects.all():
            if i.id == id:
                return i.email

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    @staticmethod
    def set_profile_email(email):
        l1.append(email)

    @staticmethod
    def get_profile_email():
        return l1[-1];

    @staticmethod
    def get_profile_id(email):
        for i in Customer.objects.all():
            if i.email == email:
                return i.id

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
    @staticmethod
    def get_fname(email):
        for i in Customer.objects.all():
            if i.email == email:
                return i.first_name
    @staticmethod
    def get_lname(email):
        for i in Customer.objects.all():
            if i.email == email:
                return i.last_name
    @staticmethod
    def get_phone(email):
        for i in Customer.objects.all():
            if i.email == email:
                return i.phone

    @staticmethod
    def otpgen():
        otp = ""
        for i in range(4):
            otp += str(r.randint(1, 9))
        otp2=int(otp)
        l.append(otp2)
        return otp
    @staticmethod
    def check_otp(otp):
        if otp in l:
            return True
        else:
            return False

    @staticmethod
    def get_lastid():
        for i in Customer.objects.all():
            k=i.id
        return k

    @staticmethod
    def email_check(email):
        for i in Customer.objects.all():
            if i.email == email:
                l2.append(email)

                return True

    @staticmethod
    def get_email():
        print(l)
        return l2[-1]

    @staticmethod
    def get_customer_by_id(id):
        return Customer.objects.filter(id__in=id)

    @staticmethod
    def set_e(k):
        l3.append(k)

    @staticmethod
    def get_e():
        return l3[-1]

    @staticmethod
    def set_email1(email):
        l4.append(email)

    @staticmethod
    def get_email1():
        return l4[-1]

    @staticmethod
    def set_eemail(email):
        l5.append(email)
        return l5[0]
    @staticmethod
    def set_email123(email):
        l6.append(email)
        print(email)

    @staticmethod
    def get_email123():
        print(l6)
        return l6[-1]





        