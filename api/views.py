from django.db.models import query
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from .sslcommerz import sslcommerz_payment_gateway
# from sslcommerz_lib import SSLCOMMERZ
# Create your views here.

# # SSLCommerz section

# settings = { 'store_id': 'bubt5b121f71beffd', 'store_pass': 'bubt5b121f71beffd@ssl', 'issandbox': True } 
# sslCommerzSetting = SSLCOMMERZ(settings)




# post_body = {}
# post_body['total_amount'] = 100.26
# post_body['currency'] = "BDT"
# post_body['tran_id'] = "12345"
# post_body['success_url'] = " http://127.0.0.1:8000/success"
# post_body['fail_url'] = " http://127.0.0.1:8000/search"
# post_body['cancel_url'] = " http://127.0.0.1:8000/cancel"
# post_body['emi_option'] = 0
# post_body['cus_name'] = "test"
# post_body['cus_email'] = "test@test.com"
# post_body['cus_phone'] = "01700000000"
# post_body['cus_add1'] = "customer address"
# post_body['cus_city'] = "Dhaka"
# post_body['cus_country'] = "Bangladesh"
# post_body['shipping_method'] = "NO"
# post_body['multi_card_name'] = ""
# post_body['num_of_item'] = 1
# post_body['product_name'] = "Test"
# post_body['product_category'] = "Test Category"
# post_body['product_profile'] = "general"


# response = sslCommerzSetting.createSession(post_body) # API response
# print(response)











class search(TemplateView):
   template_name = 'search.html'

class searchResult(ListView):
   model = Student
   def get_queryset(self):
      query = self.request.GET.get('q')
      object_list = Student.objects.filter(Q(s_id__icontains = query)|Q(p_usename__icontains = query))
      return object_list

   
   

def index(request):
    posts = "index"
    context = {
       'posts': posts
    }
  
    return render(request, 'index.html', context)





def c_first(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'c_first.html', context)


def c_second(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'c_second.html', context)


def c_third(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'c_third.html', context)


def c_fourth(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'c_fourth.html', context)


def committees(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'committees.html', context)


def confirmation(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'confirmation.html', context)


def contact(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'contact.html', context)


def edit(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'edit.html', context)


def eligible(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'eligible.html', context)


def gallery(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'gallery.html', context)

def goldmadelists(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'goldmadelists.html', context)


def payment(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'payment.html', context)



def registration(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'registration.html', context)


def rules(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'rules.html', context)

def schedule(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'schedule.html', context)


def speech_detail(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'speech_detail.html', context)

def speech(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'speech.html', context)

def venu(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'venu.html', context)

