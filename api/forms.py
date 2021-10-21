from django import forms
from . models import *

p_usename = Student.p_usename
s_id = Student.s_id
intake = Student.intake
section = 0
std_full_name = Student.std_full_name
Cell_Phone = Student.Cell_Phone
email = Student.email
totalMejor = Student.totalMejor
paidFor = Student.paidFor
hasPaid = Student.hasPaid


class RegistrationForm(forms.ModelForm):
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
    'paidFor',
    'totalPaid'
    ]