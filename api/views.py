from django.db.models import query, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from users.models import User
from .sslcommerz import sslcommerz_payment_gateway


# # SSLCommerz section


# sslCommerzSetting = SSLCOMMERZ(settings)

class PaymentView(TemplateView):

    template_name = "payment/main.html"
    

def PayView(request):
    #student = Student.objects.get(s_id = s_id)


    name = request.POST['name']
    sid = request.POST['sid']
    amount = request.POST['amount']
    return redirect(sslcommerz_payment_gateway(request, name, sid, amount))


@method_decorator(csrf_exempt, name='dispatch')

class CheckoutSuccessView(View):
    model = Transaction
    template_name = 'payment/success.html'

    
    def get(self, request, *args, **kwargs):

        # return render(request, self.template_name,{'transaction':transaction})
        return HttpResponse('nothing to see')

    def post(self, request, *args, **kwargs):

        data = self.request.POST

        #user = get_object_or_404(User, id=data['value_c']) #value_a is a user instance
        # cart = get_object_or_404(Cart, id = data['value_b'] ) #value_b is a user cart instance
        
        try:
            Transaction.objects.create(
                name = data['value_a'],
                sid = data['value_b'],
                tran_id=data['tran_id'],
                val_id=data['val_id'],
                amount=data['amount'],
                card_type=data['card_type'],
                card_no=data['card_no'],
                store_amount=data['store_amount'],
                bank_tran_id=data['bank_tran_id'],
                status=data['status'],
                tran_date=data['tran_date'],
                currency=data['currency'],
                card_issuer=data['card_issuer'],
                card_brand=data['card_brand'],
                card_issuer_country=data['card_issuer_country'],
                card_issuer_country_code=data['card_issuer_country_code'],
                verify_sign=data['verify_sign'],
                verify_sign_sha2=data['verify_sign_sha2'],
                currency_rate=data['currency_rate'],
                risk_title=data['risk_title'],
                risk_level=data['risk_level'],

            )
            messages.success(request,'Payment Successfull')


            sid = data['value_b']
            

            

        except:
            messages.success(request,'Something Went Wrong')

        
        

            
        context = {
                'sid': sid
                 }

        return render(request, 'payment/success.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutFaildView(View):
    template_name = 'payment/faild.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)












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


def confirmation(request, sid):
    
    data = Transaction.objects.get(sid = sid) 
    context = {
       'data': data
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
    posts = Student.objects.all()
    context = {
       'students': posts
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

