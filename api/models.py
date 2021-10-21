from enum import unique
from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File



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
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 1)



class Student(models.Model):
    p_usename = models.CharField(verbose_name = 'Degree', max_length=50,null = False, blank=False)
    s_id = models.IntegerField(verbose_name = 'Student ID',  unique = True, null = False, blank = False)
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


class Slider(models.Model):
    title = models.CharField(verbose_name = 'Slider Name', max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='Slider/', blank = True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    def __str__(self):
        return self.title 

class chart(models.Model):
    ChName = models.CharField(verbose_name = 'Chart Name', max_length=50,null = False, blank=False)
    TotalGra = models.IntegerField(verbose_name = 'total student', null = False, default=0, blank=False)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    
    def __str__(self):
        return self.title  