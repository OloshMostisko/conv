from enum import unique
from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File
from django.urls import reverse
from users.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=50) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image


class ConvocationLogo(models.Model):
    title = models.CharField(verbose_name = 'Convocation Name', max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='ConvocationLogo/', blank = True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)



class Student(models.Model):
    p_usename = models.CharField(verbose_name = 'Degree', max_length=50,null = False, blank=False, default="")
    s_id = models.IntegerField(verbose_name = 'Student ID',  unique = True, null = False, blank = False, default= 0)
    intake = models.IntegerField( verbose_name = 'Intake', blank=False, null=False)
    std_full_name = models.CharField( verbose_name = 'Name', max_length=100, null=False, blank=True, default="")
    Cell_Phone = models.IntegerField( verbose_name = 'Phone', null=False, blank=True, default=0)
    email = models.EmailField( verbose_name = 'Email', null = False, blank=True, default= "")

    totalMejor = models.IntegerField( verbose_name = 'Total Major',  null=False, default=0, blank=True)
    paidFor = models.IntegerField( verbose_name = 'Paid For Major',  null=False, default=0, blank=True)
   
    hasPaid = models.BooleanField( verbose_name = 'Payment Done',null=False, default=False)
    regDate = models.DateField(verbose_name = 'Registration Date', auto_now = True)
 #   published = models.DateField('Published', blank=True, null=True)
    

    def __str__(self):
        return self.std_full_name
    def get_absolute_url(self):
        return reverse('api:students', kwargs={'slug': self.slug})


class Slider(models.Model):
    title = models.CharField(verbose_name = 'Slider Name', max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='Slider/', blank = True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title 

class chart(models.Model):
    ChName = models.CharField(verbose_name = 'Chart Name', max_length=50,null = False, blank=False)
    TotalGra = models.IntegerField(verbose_name = 'total student', null = False, default=0, blank=False)
    updated_on = models.DateTimeField(auto_now  = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    
    def __str__(self):
        return self.title  


class PaymentGatewaySettings(models.Model):

    store_id = models.CharField(max_length=500, blank=True, null=True)
    store_pass = models.CharField(max_length=500, blank=True, null=True)
    issandbox = models.BooleanField(null= False, default=True)
    class Meta:
        verbose_name = "PaymentGatewaySetting"
        verbose_name_plural = "PaymentGatewaySettings"
        db_table = "paymentgatewaysettings"

class Transaction(models.Model):

   # user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # biling_profile = models.ForeignKey(Billing, on_delete=models.DO_NOTHING)
    # products    = models.ManyToManyField(Course, blank=True)
    name = models.CharField(max_length=150)
    s_id = models.IntegerField(verbose_name = 'Student ID',  unique = True, null = False, blank = False, default= 0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tran_id = models.CharField(max_length=15)
    val_id = models.CharField(max_length=75)
    card_type = models.CharField(max_length=150)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_no = models.CharField(max_length=55, null=True)
    bank_tran_id = models.CharField(max_length=155, null=True)
    status = models.CharField(max_length=55)
    tran_date = models.DateTimeField()
    currency = models.CharField(max_length=10)
    card_issuer = models.CharField(max_length=255)
    card_brand = models.CharField(max_length=15)
    card_issuer_country = models.CharField(max_length=55)
    card_issuer_country_code = models.CharField(max_length=55)
    currency_rate = models.DecimalField(max_digits=10, decimal_places=2)
    verify_sign = models.CharField(max_length=155)
    verify_sign_sha2 = models.CharField(max_length=255)
    risk_level = models.CharField(max_length=15)
    risk_title = models.CharField(max_length=25)