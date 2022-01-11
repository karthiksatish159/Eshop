from django.conf.urls import url
from django.contrib import admin
from django.http import response
from django.urls import path

from .views.address import Address, Address1
from .views.contact import Contact
from .views.contact1 import Contact1
from .views.detail import Detail
from .views.edit import Edit
from .views.edit1 import Edit1
from .views.edit2 import Edit2
from .views.filter import Filter
from .views.forgot import Forgot
from .views.forgot1 import Forgot1
from .views.forgot2 import Forgot2
from .views.otp import Otp
from .views.otp_pass import OTP_PASS
from .views.pay2 import Pay2
from .views.pay3 import Pay3
from .views.pay4 import Pay4
from .views.pay5 import Pay5
from .views.payment import Payment
from .views.pie_chart import Pie_chart

from .views.cart import Cart
from .views.checkout import CheckOut
from .views.home import Index
from .views.orders import OrderView
from .views.polls import Poll
from .views.profile import Profile
from .views.resultData import ResultData
from .views.results import Results
from .views.search import Search
from .views.show import Show
from .views.signup import Signup
from .views.login import Login, logout
from .middlewares.auth import auth_middleware
from . import views
from .views.vote import Vote

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='Logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('dashboard', Pie_chart.as_view(), name='dashboard_with_pivot'),
    path('forgot', Forgot.as_view(), name='Forgot'),
    path('forgot1', Forgot1.as_view(), name='Forgot1'),
    path('forgot2', Forgot2.as_view(), name='Forgot2'),
    path('search', Search.as_view(), name="search"),
    path('payment', Payment.as_view(), name='Payment'),
    path('otp', Otp.as_view(), name='otp'),
    path('otp_pass', OTP_PASS.as_view(), name='otp'),
    path('profile', Profile.as_view(), name='profile'),
    path('show<int:id>', Show.as_view(), name='show'),
    path('edit<int:id>', Edit.as_view(), name='edit'),
    path('edit1/<int:id>', Edit1.as_view(), name='edit1'),
    path('edit2/<int:id>', Edit2.as_view(), name='edit2'),
    path('payment2',Pay2.as_view(),name='pay2'),
    path('payment3',Pay3.as_view(),name='pay3'),
    path('payment4',Pay4.as_view(),name='pay4'),
    path('pay5',Pay5.as_view(),name='pay5'),
    path('contact',Contact.as_view(),name='contact'),
    path('contact1',Contact1.as_view(),name='contact1'),
    path('polls/', Poll.as_view(), name='index'),
    path('<int:question_id>/', Detail.as_view(), name='detail'),
    path('<int:question_id>/results/', Results.as_view(), name='results'),
    path('<int:question_id>/vote/', Vote.as_view(), name='vote'),
    path('polls/resultsdata/<str:obj>/', ResultData.as_view(), name="resultsdata"),
    path('filter',Filter.as_view(),name="Filter"),
    path('add',Address1.as_view(),name='Address')




]
