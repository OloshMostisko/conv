import string
import random
from django.conf import settings

from sslcommerz_lib import SSLCOMMERZ
from users.models import User
from .models import Hosturl, PaymentGatewaySettings, SslStoreurl
from django.http import HttpResponse, HttpResponseRedirect


def unique_trangection_id_generator(size=9, chars= string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

    

def sslcommerz_payment_gateway(request,name, s_id, amount, email,phone):
 
    gateway_auth_details = PaymentGatewaySettings.objects.all().first()
    #settings = {'store_id': gateway_auth_details.store_id, 'store_pass': gateway_auth_details.store_pass,'issandbox': gateway_auth_details.issandbox} 
    # settings = {'store_id': 'djang5ff490545f3ef',
    #         'store_pass':'djang5ff490545f3ef@ssl','issandbox': True} 
    
    settings = { 'store_id': 'djang5ff490545f3ef', 'store_pass': 'djang5ff490545f3ef@ssl', 'issandbox': True }     
    #settings = { 'store_id': 'bubtlive', 'store_pass': '5B03E0C712D6091589', 'issandbox': False } 
    
 
    urls = Hosturl.objects.all().first()
    #siteUrl = urls.siteUrl

    success = 'http://127.0.0.1:8000/success'
    faild = 'http://127.0.0.1:8000/faild'
    cancle = 'http://127.0.0.1:8000/faild'
      
    sslcommerz = SSLCOMMERZ(settings)
    tid:str = 'SSL'+unique_trangection_id_generator()
    print("Transction  ID")
    print(tid)
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
    post_body['cus_country'] = 'Bangladesh'
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    # OPTIONAL PARAMETERS
    post_body['value_a'] = name
    post_body['value_b'] = s_id
    post_body['value_c'] = email 
    post_body['value_d'] = phone


    response = sslcommerz.createSession(post_body)
    
    print("response")    
    print(response)

 
    # return HttpResponse(response)
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]
    #return 'https://securepay.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]