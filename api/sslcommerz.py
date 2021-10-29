import string
import random
from django.conf import settings

from sslcommerz_lib import SSLCOMMERZ
from users.models import User
from .models import Hosturl, PaymentGatewaySettings
from django.http import HttpResponse, HttpResponseRedirect


def unique_trangection_id_generator(size=9, chars= string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

    

def sslcommerz_payment_gateway(request,name, s_id, ssid, email, phone, amount,paidfor):
 
    gateway_auth_details = PaymentGatewaySettings.objects.all().first()
    #settings = {'store_id': gateway_auth_details.store_id,
            #'store_pass': gateway_auth_details.store_pass,'issandbox': gateway_auth_details.issandbox} 
    settings = {'store_id': 'djang5ff490545f3ef',
            'store_pass':'djang5ff490545f3ef@ssl','issandbox': True} 
    
    # settings = { 'store_id': 'bubt5b121f71beffd', 'store_pass': 'bubt5b121f71beffd@ssl', 'issandbox': True } 

 
    urls = Hosturl.objects.all().first()
    siteUrl = urls.siteUrl

    success = siteUrl+'success'
    faild = siteUrl+'faild'
    cancle = siteUrl+'faild'
      
    sslcommerz = SSLCOMMERZ(settings)
    tid:str = 'SSL'+ unique_trangection_id_generator()
    print("Transction  ID")
    print(tid)
    # post_body = {}
    # post_body['total_amount'] = amount
    # post_body['currency'] = "BDT"
    # post_body['tran_id'] = unique_trangection_id_generator()
    # post_body['success_url'] = success
    # post_body['fail_url'] = faild
    # post_body['cancel_url'] = cancle
    # post_body['emi_option'] = 0
    # post_body['cus_name'] = name
    # post_body['cus_email'] = 'request.data["email"]'
    # post_body['cus_phone'] = 'request.data["phone"]'
    # post_body['cus_add1'] = 'request.data["address"]'
    # post_body['cus_city'] = 'request.data["address"]'
    # post_body['cus_country'] = 'Bangladesh'
    # post_body['shipping_method'] = "NO"
    # post_body['multi_card_name'] = ""
    # post_body['num_of_item'] = 1
    # post_body['product_name'] = "Test"
    # post_body['product_category'] = "Test Category"
    # post_body['product_profile'] = "general"

    # # OPTIONAL PARAMETERS
    # post_body['value_a'] = phone
    # post_body['value_b'] = s_id
    # post_body['value_c'] = email
    # post_body['value_d'] = sid2 
    # post_body['value_e'] = name
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = tid
    post_body['success_url'] = success
    post_body['fail_url'] = faild
    post_body['cancel_url'] = cancle
    post_body['emi_option'] = 0
    post_body['cus_name'] = name
    post_body['cus_email'] = 'request.data["email"]'
    post_body['cus_phone'] = 'request.data["phone"]'
    post_body['cus_add1'] = 'request.data["address"]'
    post_body['cus_city'] = 'request.data["address"]'
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['num_of_item'] = paidfor
    post_body['product_name'] = "Convocation Payment"
    post_body['product_category'] = "Registration"
    post_body['product_profile'] = "Student"

    post_body['value_a'] = email
    post_body['value_b'] = phone
    post_body['value_c'] = s_id
    post_body['value_d'] = ssid
    post_body['value_e'] = name

    response = sslcommerz.createSession(post_body)
    
    print("response")    
    print(response)

    if response['status'] == 'SUCCESS':
        #return HttpResponseRedirect(response['GatewayPageURL'])
        return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]
    return HttpResponse(response)
    # response = sslcommez.createSession(post_body)
    # return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]