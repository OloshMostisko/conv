from enum import unique
from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File
from django.http import request
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
    im.save(im_io, 'JPEG', quality=35) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image


class ConvocationLogo(models.Model):
    title = models.CharField(verbose_name = 'Convocation Name', max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='ConvocationLogo/', blank = True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)

    def __str__(self):
        return self.title
class ConvocationList(models.Model):
    title = models.CharField(max_length=250, unique=True, default="")
    lstOrder = models.CharField(max_length=3, blank=False, default="", unique=True)
    slug = models.SlugField(default="", unique=True)


    class Meta:
        ordering = ["-lstOrder"]
        verbose_name = 'Previous Convocation'
        verbose_name_plural = 'Previous Convocations'

    def __str__(self):
        return self.title

    def get_absoulte_url(self):
        return reverse('convocationlists:list_by_convocationlists', args=[self.slug])
    

class Convocation(models.Model):
    title = models.CharField(verbose_name = 'Convocation Name', max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='ConvocationLogo/', blank = True)
    details = RichTextField(blank=True, null=True)
    convocation = models.ForeignKey(ConvocationList, on_delete= models.CASCADE, verbose_name ="ConvocationList", blank = False, default="")
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title

class Venu(models.Model):
    title = models.CharField(max_length=50,null = False, blank=False)
    convocation = models.ForeignKey(ConvocationList, on_delete= models.CASCADE, verbose_name ="ConvocationList", blank = False, default="")
    photo = models.ImageField(upload_to='Venu/', blank = True)
    details = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title

class Rules(models.Model):
    title = models.CharField(max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='Rules/', blank = True)
    details = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title

class ProSchedule(models.Model):
    title = models.CharField(max_length=50,null = False, blank=False)
    convocation = models.ForeignKey(ConvocationList, on_delete= models.CASCADE, verbose_name ="ConvocationList", blank = False, default="")
    photo = models.ImageField(upload_to='Venu/', blank = True)
    details = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title

class CommitteeList(models.Model):
    title = models.CharField(max_length=250, unique=True, default="")
    lstOrder = models.CharField(max_length=3, blank=False, default="", unique=True)
    slug = models.SlugField(default="", unique=True)


    class Meta:
        ordering = ["-lstOrder"]
        verbose_name = 'Program Committee'
        verbose_name_plural = 'Program Committees'

    def __str__(self):
        return self.title

    def get_absoulte_url(self):
        return reverse('committeelists:list_by_committeelists', args=[self.slug])

class Committee(models.Model):
    title = models.CharField(max_length=50,null = False, blank=False)
    committeelist = models.ForeignKey(CommitteeList, on_delete= models.CASCADE, verbose_name ="Committee List", blank = False, default="")
    photo = models.ImageField(upload_to='Committee/', blank = True)
    details = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title

class Message(models.Model):
    title = models.CharField(max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='Message/', blank = True)
    details = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title

class Speech(models.Model):
    title = models.CharField(max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='Speech/', blank = True)
    details = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title

class Gallary(models.Model):
    title = models.CharField(max_length=50,null = False, blank=False)
    convocation = models.ForeignKey(ConvocationList, on_delete= models.CASCADE, verbose_name ="ConvocationList", blank = False, default="")
    photo = models.ImageField(upload_to='Gallary/', blank = True)
    details = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title 

class Slider(models.Model):
    title = models.CharField(verbose_name = 'Slider Name', max_length=50,null = False, blank=False)
    convocation = models.ForeignKey(ConvocationList, on_delete= models.CASCADE, verbose_name ="ConvocationList", blank = False, default="")
    photo = models.ImageField(upload_to='Slider/', blank = True)
    guest =models.CharField(verbose_name = 'Guest Name', max_length=50,null = False, blank=False,default="")
    details = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title 

class Schedule(models.Model):
    title = models.CharField(verbose_name = 'Schedule Name', max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='Schedule/', blank = True)
    details = RichTextField(blank=True, null=True)
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
        return self.ChName  


class Goldmadelists(models.Model):
    G_Name = models.CharField(verbose_name = 'Goldmadelist Name', max_length=50,null = False, blank=False)
    Program = models.CharField(verbose_name = 'Student Program', max_length=50,null = False, blank=False)
    intake = models.IntegerField(verbose_name = 'Student intake', null = False, default=0, blank=False)
    section = models.IntegerField(verbose_name = 'Student intake', null = False, default=0, blank=False)
    photo = models.ImageField(upload_to='GOldmadelist/', blank = True)
    updated_on = models.DateTimeField(auto_now  = True)
    created_on = models.DateTimeField(auto_now =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    
    def __str__(self):
        return self.G_Name 

class Student(models.Model):
    p_usename = models.CharField(verbose_name = 'Degree', max_length=50, editable=False)
    s_id = models.CharField(verbose_name = 'Student ID',max_length=11, editable=False)
    intake = models.CharField( verbose_name = 'Intake', max_length=2, editable=False)
    std_full_name = models.CharField( verbose_name = 'Name', max_length=100, default="", editable=False)
    Cell_Phone = models.CharField( verbose_name = 'Phone', max_length=11, default= "")
    email = models.EmailField( verbose_name = 'Email', max_length=100, default="")
    DOB = models.CharField( verbose_name='Dath Of Birth',default="0",max_length=50, editable=False)

    paidFor = models.IntegerField( verbose_name = 'Paid For Major', default=0)
    totalMejor = models.IntegerField( verbose_name = 'Total Major', default=0)
    degree_2_id = models.CharField( verbose_name = 'Degree 2 ID', max_length=11, blank=False, default = "")

    tranId = models.CharField(verbose_name = 'Transction ID', max_length=100, blank=True)
    totalPaid = models.IntegerField( verbose_name = 'Total Paid', default=0)
    
    hasPaid = models.BooleanField( verbose_name = 'Payment Done',default= False)
    isRegDone = models.BooleanField( verbose_name = 'Registration Done',default= False)
    regDate = models.DateField(verbose_name = 'Registration Date', auto_now = True)
 #   published = models.DateField('Published', blank=True, null=True)
    

    def __str__(self):
        return self.std_full_name
        
    def get_absolute_url(self):
        return reverse('api:students', kwargs={'slug': self.slug})


class PaymentGatewaySettings(models.Model):

    store_id = models.CharField(max_length=500, blank=True, null=True)
    store_pass = models.CharField(max_length=500, blank=True, null=True)
    issandbox = models.BooleanField(null= False, default=True)
    class Meta:
        verbose_name = "PaymentGatewaySetting"
        verbose_name_plural = "PaymentGatewaySettings"
        db_table = "paymentgatewaysettings"

    def __str__(self):
        return self.store_id

class SslStoreurl(models.Model):
    url = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.url

class Transaction(models.Model):

   # user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # biling_profile = models.ForeignKey(Billing, on_delete=models.DO_NOTHING)
    # products    = models.ManyToManyField(Course, blank=True)
    name = models.CharField(max_length=150, null = False, blank = False)
    sid = models.IntegerField(verbose_name = 'Student ID', default= 0)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default = 0)
    tran_id = models.CharField(max_length=15, verbose_name = 'Transaction ID',  unique = True)
    val_id = models.CharField(max_length=75)
    card_type = models.CharField(max_length=150)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_no = models.CharField(max_length=55, null=True)
    bank_tran_id = models.CharField(max_length=155, null=True)
    status = models.CharField(max_length=55)
    tran_date = models.DateTimeField(verbose_name = 'Transaction Date', auto_now = True)
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
    email =models.CharField(max_length=40, default="")
    cellPhone = models.CharField(max_length=20, default="")
    def __str__(self):
        return str(self.sid)


class Registration(models.Model):
    stu_id1= models.CharField(verbose_name = 'Student ID ', max_length=100,  default= "")
    stu_name =models.CharField(verbose_name = 'Student Name',max_length=40, default="")
    email = models.CharField(max_length=40, default="", null=False)
    p_username = models.CharField(max_length=50, default="")
    intake = models.CharField(max_length=5, default="")
    tran_id = models.CharField(max_length=15, unique = True)
    Cell_Phone = models.CharField( verbose_name = 'Phone',max_length=11, default="")
    totalPaid = models.CharField(max_length=10, default="")
    firstDegree_id=models.CharField(verbose_name = 'First Degree ID', max_length=11,  default= "")
    photo = models.FileField(upload_to='Student_Documents/', null=True, default = 'Student_Documents/black-solid.jpg' )  #black-solid.jpg
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now =True,verbose_name='Regstration Time')
    secondDegree_id=models.CharField(verbose_name = 'Second Degree ID', max_length=11,  default= "")

    
  
    def save(self, *args, **kwargs):
        if self.photo:
            super().save(*args, **kwargs)
            img = Image.open(self.photo.path)
            if img.height > 500 or img.width >400:
                output_size = (500,400)
                img.thumbnail(output_size)
                img.save(self.photo.path)





    class Meta:
        db_table = 'Registration'

    def __str__(self):
        return str(self.stu_id1)

class OfficeMail(models.Model):
    regOfficeEmail=models.CharField(verbose_name = 'Reg Office Email', max_length=150, blank = True, default="")
    accounceOfficeEmail=models.CharField(verbose_name = 'Accounce Email', max_length=150, blank = True, default="")
    officeEmail1=models.CharField(verbose_name = 'Other office email 1', max_length=150, blank = True, default="")
    officeEmail2=models.CharField(verbose_name = 'Other office email 2', max_length=150, blank = True, default="")
    officeEmail3=models.CharField(verbose_name = 'Other office email 3', max_length=150, blank = True, default="")
    officeEmail4=models.CharField(verbose_name = 'Other office email 4', max_length=150, blank = True, default="")
    
    
    def __str__(self):
        return str(self.regOfficeEmail)


class Hosturl(models.Model):
    siteUrl = models.CharField(max_length=100)