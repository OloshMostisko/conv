from django import forms
from . models import *

class BillingForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
    'p_usename' ,'s_id' ,
    'intake' ,
    'section' ,
    'std_full_name' ,
    'Cell_Phone' , 
    'email' ,
    'totalMejor',
    'paidFor' ,
    'hasPaid' ,
    'regDate' 
    ]