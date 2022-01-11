from django.db import models

l = []
l.append('email')

class Category(models.Model):
    object = None
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

    @staticmethod
    def set_cid(categoryID):
        if categoryID==None:
            print(categoryID)
        else:
            cid=int(categoryID)
            for i in Category.objects.all():
                m=i.id
                print('sadas',m,cid)
                if m==cid:
                    print('test',i.name)
                    l.append(i.name)
            print(l)

    @staticmethod
    def get_cid():
        print("in get= ",l)
        return l[-1]
    @staticmethod
    def print1():
        print(l)




def objects():
    return None
