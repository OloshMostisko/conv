from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.urls import reverse

# Create your views here.


def index(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'index.html', context)


def c_first(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'c_first.html', context)


def c_second(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'c_second.html', context)


def c_third(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'c_third.html', context)


def c_fourth(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'c_fourth.html', context)


def committees(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'committees.html', context)


def confirmation(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'confirmation.html', context)


def contact(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'contact.html', context)


def edit(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'edit.html', context)


def eligible(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'eligible.html', context)


def gallery(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'gallery.html', context)

def goldmadelists(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'goldmadelists.html', context)


def payment(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'payment.html', context)



def registration(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'registration.html', context)


def rules(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'rules.html', context)

def schedule(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'schedule.html', context)


def speech_detail(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'speech_detail.html', context)

def speech(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'speech.html', context)

def venu(request):
    posts = "Index"
    context = {
       'posts': posts
    }
  
    return render(request, 'venu.html', context)