from django.db.models import query
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.urls import reverse
from django.views.generic import TemplateView, ListView

# for payment
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket


bubt_store_id= 'bubt5b121f71beffd'
bubt_store_pass = 'bubt5b121f71beffd@ssl'
issandbox =  True 

success_url = 'status_url'
fail_url = 'status_url'
cancel_url = 'status_url'
ipn_url = 'status_url'


# def Confirm(request):
#     saved_form = Registration.objects.get_or_create()
#     saved_address = saved_address[0]
#     form = BillingForm(instance=saved_address)
#     if request.method == "POST":
#         form = BillingForm(request.POST, instance=saved_address)
#         if form.is_valid():
#             form.save()
#             form = BillingForm(instance=saved_address)
#             messages.success(request, f"Shipping Address Saved!")
#     order_qs = Order.objects.filter( ordered=False)
#     order_items = order_qs[0].orderitems.all()
#     order_total = order_qs[0].get_totals()

#     return render(request, 'App_Payment/checkout.html', context={"form":form, "order_items":order_items, "order_total":order_total, "saved_address":saved_address})

def payment(request):
    student = Student.objects.get_or_create()
    saved_student = student[0]
    if not saved_student.is_fully_filled():
        messages.info(request, f"Please Complete shipping address!")
        return redirect("App_Payment:checkout")

    if not request.user.profile.is_fully_filled():
        messages.info(request, f"Please Complete profile details!")
        return redirect("App_Login:profile")

    store_id = bubt_store_id
    API_key = bubt_store_pass
    current_user = Student
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)

    status_url = request.build_absolute_uri(reverse("App_Payment:complete"))
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

   # # order_qs = Student.objects.filter()
   #  order_items = order_qs[0].orderitems.all()
   #  order_items_count = order_qs[0].orderitems.count()
    total = 5000.00

    mypayment.set_integration(total_amount=Decimal(total), currency='BDT', Category='Student', name=current_user.std_full_name, num_of_mejor= current_user.totalMejor)
    mypayment.set_customer_info(name=current_user.std_full_name, email=current_user.email, phone=current_user.Cell_Phone)

    
    response_data = mypayment.init_payment()

    return redirect(response_data['GatewayPageURL'])




class search(TemplateView):
   template_name = 'search.html'

class searchResult(ListView):
   model = Student
   template_name = 'srcResut.html'
   def get_queryset(self):
      query = self.request.GET.get('q')
      object_list = Student.objects.filter(Q(s_id__icontains = query))
      return object_list
   

def index(request):
    posts = "Index"
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

