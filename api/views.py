from django.db.models import query, Q
from django.http.response import HttpResponseRedirect
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
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import json, re
from django.core import serializers

# # SSLCommerz section


# sslCommerzSetting = SSLCOMMERZ(settings)

class PaymentView(TemplateView):

    template_name = "payment/main.html"
    

def PayView(request):
    #student = Student.objects.get(s_id = s_id)


    name = request.POST['name']
    s_id = request.POST['s_id']
    amount = request.POST['amount']
    email = request.POST['email']
    return redirect(sslcommerz_payment_gateway(request,name, s_id, amount, email))


@method_decorator(csrf_exempt, name='dispatch')

class CheckoutSuccessView(View):
    model = Transaction
    template_name = 'payment/success.html'

    
    def get(self, request, *args, **kwargs):

        # return render(request, self.template_name,{'transaction':transaction})
        return HttpResponse('nothing to see')

    def post(self, request, *args, **kwargs):

        data = self.request.POST
        # namedata = str(data['value_a']),
        # s_iddata = str(data['value_b']),
        # emaildata = str(data['value_c']),
        # tran_iddata = str(data['tran_id']),

        # name1 = namedata.replace("(","")
        # name2 = name1.replace(")","")
        # name = str(name2.replace(",",""))

        # s_id1 = s_iddata.replace("(","")
        # s_id2 = s_id1.replace(")","")
        # s_id = s_id2.replace(",","")
        
        # tran_id1 = tran_iddata.replace("(","")
        # tran_id2 = tran_id1.replace(")","")
        # tran_id = str(tran_id2.replace(",",""))
        
        # email1 = emaildata.replace("(","")
        # email2 = email1.replace(")","")
        # email = str(email2.replace(",",""))
        
        # arr : int = []
        # arr.append(data['amount'])
        # amountf = arr[0],
        # amount: int = int(amountf),
        # amountdata = data['amount']
        # amount1 = amountdata.replace("(","")
        # amount2 = amount1.replace(")","")

        amount = int(float(data['amount']))
       

        email_id = ['imkhaled404@gmail.com','amishezanmahmud@gmail.com','imnoman404@gmail.com']
        email_id.append(data['value_c'])

        #user = get_object_or_404(User, id=data['value_c']) #value_a is a user instance
        # cart = get_object_or_404(Cart, id = data['value_b'] ) #value_b is a user cart instance

        username = data['value_a']
        allemail = email_id
        ######################### mail system ####################################
        htmly = get_template('email/Email.html')
        d = { 
            's_id' : data['value_b'],
            'username': data['value_a'], 
            'tran_id' : data['tran_id'],
            'amount'  : amount

            }
        subject, from_email, to = 'BUBT 5th Convocation Payment Confirmation', 'your_email@gmail.com', allemail
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
                ##################################################################

        # Student data update , set tran_id and paid = true

        paidfor = 0

        if (amount > 4999 and amount < 5900):
            paidfor = 1

        if (amount > 5999):
            paidfor = 2

        update_value = {
            "hasPaid" : True,
            "tranId" :  data['tran_id'],
            "paidFor" : paidfor,
            "paidAmount" : data['amount']
        }
        obj, created = Student.objects.update_or_create(s_id= data['value_b'], defaults=update_value)

        ###########################

        try:
            Transaction.objects.create(
                name = data['value_a'],
                sid = data['value_b'],
                email = data['value_c'],
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

        except:
            messages.success(request,'Something Went Wrong')
          
        context = {
                's_id': data['value_b'],
                'name' : data['value_a'],
                'tran_id' : data['tran_id'],
                'email' : data['value_c']
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
        totalTransction  = Transaction.objects.count()
        query = self.request.GET.get('q')

        if  totalTransction > 980:
            return HttpResponse('<h1>Page not found</h1>')
        else:
            object_list = Student.objects.filter(Q(s_id__icontains = query)|Q(p_usename__icontains = query))
            return object_list





class paymentSearch(TemplateView):
   template_name = 'Reg/paySearch.html'

class paySearchResult(ListView):
    model = Transaction
    
    def get_queryset(self):
        totalTransction  = Transaction.objects.count()
        query = self.request.GET.get('q')
        #query = self.request.GET.get('tid')

        if  totalTransction > 980:
            return HttpResponse('<h1>Page not found</h1>')
        else:
            object_list = Transaction.objects.filter(Q(tran_id__icontains = query)&Q(sid__icontains = query))

            return object_list



class RegistrationView(TemplateView):

    template_name = "Reg/main.html"
    

def RegistrationView(request):
    #student = Student.objects.get(s_id = s_id)


    name = request.POST['name']
    s_id = request.POST['s_id']
    amount = request.POST['amount']
    email = request.POST['email']
    #return HttpResponse('<h1>Page not found</h1>')
    return (request,name, s_id, amount, email)

def index(request):
    posts = "index"
    slider = Slider.objects.all()
    context = {
       'posts': posts,
       'slider': slider
    }
  
    return render(request, 'index.html', context)

def chart(request):
    posts = chart.objects.all()
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'index.html', context)

def slider(request):
    posts = Slider.objects.all()
    context = {
       'posts': posts
    } 
  
    return render(request, 'index.html', context)


def c_first(request):
    posts = Convocation.objects.filter(convocation__title = '1st Convocation')
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'c_first.html', context)


def c_second(request):
    posts = Convocation.objects.filter(convocation__title = '2nd Convocation')
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'c_second.html', context)


def c_third(request):
    posts = Convocation.objects.filter(convocation__title = '3rd Convocation')
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'c_third.html', context)


def c_fourth(request):
    posts = Convocation.objects.filter(convocation__title = '4th Convocation')
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'c_fourth.html', context)


def committees(request):
    posts = Committee.objects.all()
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'committees.html', context)


def confirmation(request, s_id, name):
    
   # data = Transaction.objects.get(s_id = s_id) 
    context = {
      # 'data': data
    }
  
    return render(request, 'confirmation.html', context)


def contact(request):
    posts = "contact"
    context = {
       'posts': posts
    }
  
    return render(request, 'contact.html', context)


# def edit(request):
#     posts = .objects.all()
#     context = {
#        'posts': posts.order_by('-created_on')
#     }
  
#     return render(request, 'edit.html', context)
# after updating it will redirect to detail_View
def edit(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = Student.objects.get(id = id)
          
    return render(request, "edit.html", context)
 
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Student, id = id)
 
    # pass the object as instance in form
    form = Student(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

def eligible(request):
    posts = Student.objects.all()
    context = {
       'students': posts
    }
  
    return render(request, 'eligible.html', context)


def gallery(request):
    posts = Gallary.objects.all()
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'gallery.html', context)

def goldmadelists(request):
    posts = Goldmadelists.objects.all()
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'goldmadelists.html', context)


def payment(request):
    posts = "Index"
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'payment.html', context)



def registration(request):
    allStudent = Student.objects.all()
    isPaid = Student.objects.filter(Q(hasPaid = True))
    
    context = {
       'allStudent' : allStudent,
       'isPaid' : isPaid
    }
  
    return render(request, 'registration.html', context)


def rules(request):
    posts = Rules.objects.all()
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'rules.html', context)

def schedule(request):
    posts = Schedule.objects.all()
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'schedule.html', context)


def speech_detail(request,post_id):
    posts = Speech.objects.get(pk=post_id)
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'speech_detail.html', context)

def speech(request):
    posts = Speech.objects.all()
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'speech.html', context)

def venu(request):
    posts = Venu.objects.all()
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'venu.html', context)

def convocationlogo(request):
    posts = ConvocationLogo.objects.all()
    context = {
       'posts': posts.order_by('-created_on')
    }
  
    return render(request, 'base.html', context)