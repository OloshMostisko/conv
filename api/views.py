import os
from django.contrib.auth import forms
from django.db.models import query, Q
from django.http.response import Http404, HttpResponseRedirect
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
from django.core.mail import message, send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core import serializers
from django.template import Context, RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_protect
import json, re, string ,random
from django.core.files.storage import FileSystemStorage
from types import SimpleNamespace

from .forms import * 
from urllib.parse import urlparse


def unique_trangection_id_generator(size=9, chars=  string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



class PaymentView(TemplateView):

    template_name = "payment/main.html"
    


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        std_id = self.kwargs.get('s_id')
        print(std_id)
        student = get_object_or_404(Student, s_id=std_id)
        print(student)
        data['std_fullname'] = student.std_full_name
        return data

def PayView(request):

    name = request.POST['name']
    email = request.POST['email']
    s_id = request.POST['s_id']
    phone = request.POST['phone']
    paidfor = request.POST['paidfor']
    if paidfor == "2":
        amount = 12
    else:
        amount = 10
    ssid = "x"
    sid2 = request.POST['sid2']
    
    de1 = Student.objects.filter(s_id = s_id).first()
    
    totalTransction  = Transaction.objects.count()
    if totalTransction >= 980:
        return HttpResponse('<h1>Registration Limit over </h1>')
    else:
        if not de1:
            return HttpResponse('<h1>Student is not eligible </h1>') 
        else:
            plen = len(phone)
            if plen != 11 :
                return HttpResponse('<h1>Student Phone no must 11 digit</h1>')
                    
            else:
                if email == "" :
                    return HttpResponse('<h1>Student Email </h1>')
                else:
                    if paidfor == "" :
                        return HttpResponse('<h1>Error</h1>')
                    else:
                        if paidfor =="2":
                            s2len = len(sid2)
                            if s2len < 9:
                                return HttpResponse('<h1>Double Degree Student ID Wrong</h1>')
                            else:
                                ssid = sid2
                                de2 = Student.objects.filter(s_id = sid2).first()
                                if not de2:
                                    return HttpResponse('<h1>Double Degree not exist.</h1>')
                                else:

                                    dob1 = de1.DOB
                                    dob2 = de2.DOB
                                    print(dob1)
                                    print(dob2)
                                    if de1.DOB != de2.DOB or de1.std_full_name != de2.std_full_name:
                                        return HttpResponse('<h1>Double Degree Student not same..</h1>')
                                    else:
                                        update_value = {               
                                            "Cell_Phone" :phone,
                                            "totalMejor" :  paidfor,
                                            "email" : email,
                                            "degree_2_id" : ssid,
                                        }
                                        obj, created = Student.objects.update_or_create(s_id= s_id,  defaults=update_value)
                                        try:                                
                                            Registration.objects.create(                                    
                                                stu_id1 = s_id,
                                                stu_name = name,
                                                email =  email,
                                                p_username = "",
                                                intake = "",
                                                tran_id = "",
                                                Cell_Phone =  phone,
                                                totalPaid =  "",
                                                firstDegree_id =  s_id,
                                                secondDegree_id = ssid,
                                            
                                            )
                                            messages.success(request,'Registration Created')

                                        except:
                                            messages.success(request,'Registration Create Failed')


                                        return redirect(sslcommerz_payment_gateway(request,name, s_id, amount, email,phone)) 
                        else:
                            ssid = ""
                            update_value = {               
                                            "Cell_Phone" :phone,
                                            "totalMejor" :  paidfor,
                                            "email" : email,
                                            "degree_2_id" : ssid,
                                        }
                            obj, created = Student.objects.update_or_create(s_id= s_id, defaults=update_value)
                            try:                                
                                Registration.objects.create(                                    
                                    stu_id1 = s_id,
                                    stu_name = name,
                                    email =  email,
                                    p_username = "",
                                    intake = "",
                                    tran_id = "",
                                    Cell_Phone =  phone,
                                    totalPaid =  "",
                                    firstDegree_id =  s_id,
                                    secondDegree_id = ssid,
                                  
                                )
                                messages.success(request,'Registration Created')

                            except:
                                messages.success(request,'Registration Create falied')
                      
                          
                            return redirect(sslcommerz_payment_gateway(request,name, s_id, amount, email,phone)) 
 


 #return redirect(sslcommerz_payment_gateway(request,name, s_id,sid2, amount, email)) 
@method_decorator(csrf_exempt, name='dispatch')
class CheckoutSuccessView(View):
    model = Transaction
    template_name = 'payment/success.html'

    
    def get(self, request, *args, **kwargs):

        # return render(request, self.template_name,{'transaction':transaction})
        return HttpResponse('nothing to see')

    def post(self, request, *args, **kwargs):

        data = self.request.POST
        
        print(data)
        ddata = json.dumps(data)
        print("Loaded data")
        load = json.loads(ddata)
   
       
        name : str = load['value_a']
        amount = int(float(data['amount']))
        tid: str = load['tran_id']
        email : str = load['value_c']
        phone  : str = load['value_d']
        s_id : str = load['value_b']
        #ssid : str = load['value_d']

        paidfor = "1"
        print( amount, tid, email, phone, s_id)
        if amount > 6498 :
            paidfor = "2"
        else:
            paidfor = "1"
        ###########################
        update_value = {
            
                                    
            "Cell_Phone" :data['value_d'],
            "hasPaid" : True,
            "tranId" : data['tran_id'],
            "paidFor" : paidfor,
            "totalMejor" :  paidfor,
            "email" : data['value_c'],
            "totalPaid" : amount,
            "isRegDone": False

        }
        obj, created = Student.objects.update_or_create(s_id= s_id, defaults=update_value)
        
        sdata = Student.objects.filter(s_id = data['value_b'])
        
        
        ###### mail system ###########
        mail = OfficeMail.objects.all().first()
        regEmail = mail.regOfficeEmail
        accEmail = mail.accounceOfficeEmail
        email1 = mail.officeEmail1
        email2 = mail.officeEmail2
        email3 = mail.officeEmail3
        email4 = mail.officeEmail4

        email_id = []
     
        email_id.append(data['value_a'])
        email_id.append(regEmail)
        email_id.append(accEmail)
        email_id.append(email1)
        email_id.append(email2)
        email_id.append(email3)
        email_id.append(email4)
        
        allemail = email_id
       
        htmly = get_template('email/Email.html')
       
        username = ""
        print(username)
        d = { 
            "s_id" : data['value_b'],
            "username" : data['value_a'], 
            "tran_id" : data['tran_id'],
            "amount"  : amount

            }
        subject, from_email, to = 'BUBT 5th Convocation Registration payment', 'your_email@gmail.com', allemail
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        ###### mail system ###########
                ##################################################################

        # Student data update , set tran_id and paid = true

        #paidfor = data['value_e']

      
        cell = str(data['value_c'])
        print(cell)


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
                email = data['value_c'],
                cellPhone = data['value_d']

            )
            messages.success(request,'Payment Successfull')
         
            updatevalue = {
                    "stu_id1" : data['value_b'],
                    "stu_name" : data['value_a'],
                    "email" :  data['value_c'],
                    "tran_id" :  data['tran_id'],
                    "Cell_Phone" :  data['value_d'],
                    "totalPaid" :  data['amount'],
                    "firstDegree_id" :  data['value_b'],

                }
            obj, created = Registration.objects.update_or_create(stu_id1= s_id, defaults=updatevalue)
            messages.success(request,'Registration Created')
            
        except:
            messages.success(request,'Something Went Wrong')

        context = {
                's_id': data['value_b'],
                'name' : data['value_a'],
                'tran_id' : data['tran_id'],
                'email' : data['value_c'],
                'totalPaid' :  data['amount'],
                 }
        return render(request, 'payment/success.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutFaildView(View):
    template_name = 'payment/faild.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)



#payment from accounce
@method_decorator(login_required, name='dispatch')
class PaymentView2(TemplateView):

    template_name = "payment/main2.html"


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        std_id = self.kwargs.get('s_id')
        student = get_object_or_404(Student, s_id=std_id)
        data['std_fullname'] = student.std_full_name
        return data

def PayView2(request):
    transaction_data = None
    saved_registration = None

    name = request.POST['name']
    email = request.POST['email']
    s_id = request.POST['s_id']
    phone = request.POST['phone']
    paidfor = request.POST['paidfor']


    tid : str = 'ACC'+unique_trangection_id_generator()
    if paidfor == "2":
        amount = 6500
    else:
        amount = 5000
    ssid = "x"
    sid2 = request.POST['sid2']
    de1 = Student.objects.filter(s_id = s_id).first()

    
    totalTransction  = Transaction.objects.count()
    if totalTransction and totalTransction > 980:
        return HttpResponse('<h1>Registration Limit over </h1>')
    else:
        if not de1:
            return HttpResponse('<h1>Student is not eligible </h1>') 
        else:
            plen = len(phone)
            if plen != 11 :
                return HttpResponse('<h1>Student Phone no must 11 digit</h1>')
                    
            else:
                if email == "" :
                    return HttpResponse('<h1>Student Email </h1>')
                else:
                    if paidfor == "" :
                        return HttpResponse('<h1>Error</h1>')
                    else:
                        if tid == "":
                                return HttpResponse('<h1>Put a Transtion Id</h1>')
                        else:
                            if paidfor =="2":
                                s2len = len(sid2)
                                if s2len < 9:
                                    return HttpResponse('<h1>Double Degree Student ID Wrong</h1>')
                                else:
                                    ssid = sid2
                                    de2 = Student.objects.filter(s_id = sid2).first()
                                    if not de2:
                                        return HttpResponse('<h1>Double Degree not exist.</h1>')
                                    else:

                                        dob1 = de1.DOB
                                        dob2 = de2.DOB
                                        print(dob1)
                                        print(dob2)
                                        if de1.DOB != de2.DOB:
                                            return HttpResponse('<h1>Double Degree Student not same..</h1>')
                                        else:
                                           # return  HttpResponse('<h1>Account Pay done..</h1>')
                                           amount = amount
                                update_value = {
                                    
                                    "Cell_Phone" :phone,
                                    "hasPaid" : True,
                                    "tranId" : tid,
                                    "paidFor" : paidfor,
                                    "totalMejor" : paidfor,
                                    "email" : email,
                                    "totalPaid" : str(amount),
                                    "isRegDone": False

                                }
                                obj, created = Student.objects.update_or_create(s_id= s_id, defaults=update_value)

                                mail_list = OfficeMail.objects.all()
                                email_id = []

                                for mail in mail_list:
                                    if mail:
                                        email_id.append(mail)
                                if email:
                                    email_id.append(email)
                                

                                
                                allemail = email_id
                                ######################### mail system ####################################
                                htmly = get_template('email/Email.html')
                            
                                username = ""
                                print(username)
                                d = { 
                                    "s_id" : s_id,
                                    "username" : name, 
                                    "tran_id" : tid,
                                    "amount"  : amount

                                    }
                                subject, from_email, to = 'BUBT 5th Convocation payment Confirmation', 'your_email@gmail.com', allemail
                                html_content = htmly.render(d)
                                msg = EmailMultiAlternatives(subject, html_content, from_email, to)
                                msg.attach_alternative(html_content, "text/html")
                                msg.send()
                                        #############################################

                                # Student data update , set tran_id and paid = true


                                paidfor = 0

                                if amount > 4995 and amount < 5900:
                                    paidfor = 1
                                elif amount > 6480:
                                    paidfor = 2

                                cell = phone
                                print(cell)

                                try :
                                    transaction_data= Transaction.objects.create(
                                        name = name, sid = s_id, tran_id=tid, 
                                        val_id="x",amount=amount,card_type="x",card_no="x",
                                        store_amount=0.0,bank_tran_id="Acc pay",status="ACC Pay",
                                        tran_date= "",currency="BDT",card_issuer="s", card_brand="x",
                                        card_issuer_country="x",card_issuer_country_code="x",
                                        verify_sign="X",verify_sign_sha2="X",currency_rate=0.0,
                                        risk_title="X", risk_level="X",email = email, cellPhone =phone
                                        )
                                                                
                                except Exception as e:
                                    print(f"Transaction Fined {e}")

                                
                                if transaction_data:
                                    try:
                                        saved_registration = Registration.objects.create(
                                            stu_id1 = s_id,
                                            stu_name = name,
                                            email =  email,
                                            p_username = "",
                                            intake = "",
                                            tran_id =tid,
                                            Cell_Phone =  phone,
                                            totalPaid =  str(amount),
                                            firstDegree_id =  s_id,
                                            secondDegree_id = ssid,
                                            )
                                        print("saved_registration---",saved_registration)
                                    except Exception as e:
                                        print(f"Registration Fined {e}")

                                    
                                if transaction_data and saved_registration:
                                    if s_id:
                                        obj = Student.objects.get(s_id= s_id)
                                        print("------", dir(obj))
                                        obj.Cell_Phone = phone
                                        obj.hasPaid = True
                                        obj.tranId = tid
                                        obj.paidFor = paidfor
                                        obj.totalMejor = paidfor
                                        obj.email = email
                                        obj.degree_2_id = sid2
                                        obj.totalPaid = str(amount)
                                        obj.isRegDone = False
                                        obj.save()

                                context = {
                                        
                                        'sdata' : obj,
                                        'tran_id' : tid,
                                        'email' : email
                                        }

                               # return render('payment/success.html', context)
                                return  HttpResponse(html_content)

                            elif paidfor =="1":
                                #return  HttpResponse('<h1>Account Pay done..</h1>')
                                amount = amount

                                update_value = {
                                    
                                    "Cell_Phone" :phone,
                                    "hasPaid" : True,
                                    "tranId" : tid,
                                    "paidFor" : paidfor,
                                    "degree_2_id" : sid2,
                                    "email" : email,
                                    "totalMejor" : paidfor,
                                    "totalPaid" : str(amount),
                                    "isRegDone": False

                                }
                                obj, created = Student.objects.update_or_create(s_id= s_id, defaults=update_value)
                              
                                mail = OfficeMail.objects.all().first()
                                regEmail = mail.regOfficeEmail
                                accEmail = mail.accounceOfficeEmail
                                email1 = mail.officeEmail1
                                email2 = mail.officeEmail2
                                email3 = mail.officeEmail3
                                email4 = mail.officeEmail4

                                email_id = []
                            
                                email_id.append(email)
                                email_id.append(regEmail)
                                email_id.append(accEmail)
                                email_id.append(email1)
                                email_id.append(email2)
                                email_id.append(email3)
                                email_id.append(email4)
                                
                                allemail = email_id
                                ######################### mail system ####################################
                                htmly = get_template('email/Email.html')
                            
                                username = ""
                                print(username)
                                d = { 
                                    "s_id" : s_id,
                                    "username" : name, 
                                    "tran_id" : tid,
                                    "amount"  : amount

                                    }
                                subject, from_email, to = 'BUBT 5th Convocation Payment Confirmation', 'your_email@gmail.com', allemail
                                html_content = htmly.render(d)
                                msg = EmailMultiAlternatives(subject, html_content, from_email, to)
                                msg.attach_alternative(html_content, "text/html")
                                msg.send()
                                        #############################################

                                # Student data update , set tran_id and paid = true

                                paidfor = 0

                                if (amount > 4995 and amount < 5900):
                                    paidfor = 1

                                if (amount > 6000):
                                    paidfor = 2


                                cell = phone
                                print(cell)

                                try:
                                    Transaction.objects.create(
                                        name = name,
                                        sid = s_id,
                                        tran_id=tid,
                                        val_id="x",
                                        amount=amount,
                                        card_type="x",
                                        card_no="x",
                                        store_amount="x",
                                        bank_tran_id="Acc pay",
                                        status="ACC Pay",
                                        tran_date= "",
                                        currency="BDT",
                                        card_issuer="s",
                                        card_brand="x",
                                        card_issuer_country="x",
                                        card_issuer_country_code="x",
                                        verify_sign="X",
                                        verify_sign_sha2="X",
                                        currency_rate="X",
                                        risk_title="X",
                                        risk_level="X",
                                        email = email,
                                        cellPhone =phone

                                    )
                                    messages.success(request,'Payment Successfull')
                                except:
                                    messages.success(request, 'Failed')

                                try:                                                                        
                                        Registration.objects.create(                                    
                                            stu_id1 = s_id,
                                            stu_name = name,
                                            email =  email,
                                            p_username = "",
                                            intake = "",
                                            tran_id = tid,
                                            Cell_Phone =  phone,
                                            totalPaid =  str(amount),
                                            firstDegree_id =  s_id,
                                            secondDegree_id = ssid,
                                            
                                        )

                                except:
                                        messages.success(request,'Registration Create Failed')
                                update_value = {
            
                                    
                                        "Cell_Phone" :phone,
                                        "hasPaid" : True,
                                        "tranId" : tid,
                                        "paidFor" : paidfor,
                                        "totalMejor" :  paidfor,
                                        "email" : email,
                                        "degree_2_id" : sid2,
                                        "totalPaid" : str(amount),
                                        "isRegDone": False

                                    }
                                obj, created = Student.objects.update_or_create(s_id= s_id, defaults=update_value)
                                updatevalue = {
                                            "stu_id1" : s_id,
                                            "stu_name" : name,
                                            "email" :  email,
                                            "tran_id" :  tid,
                                            "Cell_Phone" :  phone,
                                            "totalPaid" :  str(amount),
                                            "firstDegree_id" :  s_id,

                                        }
                                obj, created = Registration.objects.update_or_create(stu_id1= s_id, defaults=updatevalue)
                                       

                                sdata = Student.objects.filter(s_id = s_id)
                                context = {
                                        
                                        'sdata' : sdata,
                                        'tran_id' : tid,
                                        'email' : email
                                        }

                               # return render('payment/success.html', context)
                                return  HttpResponse(html_content)
                            else:
                                return  HttpResponse('<h1>Account Pay Failed..</h1>')


class search(TemplateView):
   template_name = 'search/search.html'

class searchResult(ListView):
    model = Student
    
    def get_queryset(self):
        totalTransction  = Transaction.objects.count()
        query = self.request.GET.get('q')

        if  totalTransction >= 980:
            return HttpResponse('<h1>Page not found</h1>')
        else:
            object_list = Student.objects.filter(Q(s_id__icontains = query)|Q(p_usename__icontains = query))
            return object_list


@method_decorator(login_required, name='dispatch')
class search2(TemplateView):
   template_name = 'search/search2.html'

@method_decorator(login_required, name='dispatch')
class searchResult2(ListView):
    model = Student

    def get_queryset(self):
        totalTransction  = Transaction.objects.count()
        query = self.request.GET.get('q')
        
        if  totalTransction >= 980:
            return HttpResponse('<h1>Page not found</h1>')
        else:
            object_list = Student.objects.filter(Q(s_id__icontains = query)|Q(p_usename__icontains = query))
            return object_list



class PaymentSearch(TemplateView):
   template_name = 'reg/paysearch.html'

def PaySearchResultView(request):
        model = Student   
    #def get_queryset(self):
        
        sid  = request.GET.get('s_id')
        tid = request.GET.get('t_id')

        tidlen = len(tid)
        if tidlen >= 9:
            obj1 = Student.objects.filter(s_id = sid).first()
            obj2 = Student.objects.filter(tranId = tid).first()

            t1 = obj1.tranId
            print(t1)
            t2 = obj2.tranId
            print(t2)
            if t1 != t2 :
                return HttpResponse('<h1>Wrong Information</h1>')
            else:
                obj = Student.objects.filter(tranId = tid)
                print(obj)
                context = {
                    "obj" : obj
                }

            return render(request, 'reg/paySrcResult.html', context )

        else: 
            return HttpResponse('<h1>Wrong Transction Information</h1>')
              


def update_student(request, s_id):
    user = get_object_or_404(Registration,stu_id1 = s_id)
    if request.method=="POST":
        if len(request.FILES) != 0:
            # if len(user.photo) > 0:
            #     os.remove(user.photo.path)
            user.photo = request.FILES['img']
            
    user.stu_name = request.POST.get('name')
    user.email = request.POST.get('email')
    user.p_username = request.POST.get('dept')
    user.intake = request.POST.get('intake')

    user.Cell_Phone = request.POST.get('phone')
    user.totalPaid = request.POST.get('totalPaid')
    user.firstDegree_id = request.POST.get('sid')
    ssid = request.POST.get('ssid')
    s2 = ""

    if not ssid:
        s2 = "x"
    else: 
        s2 = request.POST.get('ssid')

    user.secondDegree_id = s2
    user.save()
    messages.success(request, "Photo Uplaoded")
    update_value = {               
    "isRegDone" :True,
   
            }
    obj, created = Student.objects.update_or_create(s_id= s_id, defaults=update_value)
        ###### mail system ###########
    mail = OfficeMail.objects.all().first()
    regEmail = mail.regOfficeEmail
    accEmail = mail.accounceOfficeEmail
    email1 = mail.officeEmail1
    email2 = mail.officeEmail2
    email3 = mail.officeEmail3
    email4 = mail.officeEmail4

    email_id = []
    
    email_id.append(user.email)
    email_id.append(regEmail)
    email_id.append(accEmail)
    email_id.append(email1)
    email_id.append(email2)
    email_id.append(email3)
    email_id.append(email4)
    
    allemail = email_id
    
    htmly = get_template('email/REmail.html')
    
    username = ""
    print(username)
    d = { 
        "s_id" : request.POST.get('sid'),
        "username" : request.POST.get('name'), 
        "dept" : request.POST.get('dept'),
        "intake"  : request.POST.get('intake')

        }
    subject, from_email, to = 'BUBT 5th Convocation Registration Confirmation', 'your_email@gmail.com', allemail
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, html_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
        ###### mail system ###########

    context = {
        'name': request.POST.get('name'),
        'sid' :  s_id,
        'dept' : request.POST.get('dept'),
        'intake' : request.POST.get('intake'),
        'totalPaid' : request.POST.get('totalPaid'),
        'email' : request.POST.get('email'),

    }
    return render(request, 'reg/regsuccess.html', context )



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

def confirmReg(request):
    posts = "contact"
    context = {
       'posts': posts
    }
  
    return render(request, 'reg/confirmReg.html', context)



def error(request):
  
    return render(request, 'error.html')