from enum import unique
from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from datetime import datetime


class Student(models.Model):
    p_usename = models.CharField(verbose_name = 'Degree', max_length=50,null = False, blank=False)
    s_id = models.IntegerField(verbose_name = 'Student ID',  unique = True, null = False, blank = False)
    intake = models.IntegerField( verbose_name = 'Intake', blank=False, null=False)
    std_full_name = models.CharField( verbose_name = 'Name', max_length=100, null=False, blank=True, default="")
    Cell_Phone = models.IntegerField( verbose_name = 'Phone', null=False, blank=True, default=0)
    emai = models.EmailField( verbose_name = 'Email', null = False, blank=True, default= "")

    totalMejor = models.IntegerField( verbose_name = 'Total Major',  null=False, default=0, blank=True)
    paidFor = models.IntegerField( verbose_name = 'Paid For Major',  null=False, default=0, blank=True)
   
    hasPaid = models.BooleanField( verbose_name = 'Payment Done',null=False, default=False)
    regDate = models.DateField(verbose_name = 'Registration Date', auto_now = True)
 #   published = models.DateField('Published', blank=True, null=True)
    

    def __str__(self):
        return self.std_full_name 

class ConvocationLogo(models.Model):
    title = models.CharField(verbose_name = 'Convocation Name', max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='ConvocationLogo/', blank = True)


    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(verbose_name = 'Slider Name', max_length=50,null = False, blank=False)
    photo = models.ImageField(upload_to='Slider/', blank = True)

    
    def __str__(self):
        return self.title  

class Slider(models.Model):
    title = models.CharField(verbose_name = 'Slider Name', max_length=50,null = False, blank=False)
    total_gradu = title = models.IntField(verbose_name = 'total student', max_length=50,null = False, blank=False)

    
    def __str__(self):
        return self.title  
