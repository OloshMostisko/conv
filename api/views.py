from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.urls import reverse
from django.views.generic import TemplateView, ListView

# Create your views here.


def index(request):
   
    posts = "Shezan Mahmud"
    
    context = {
       'posts': posts
    }
  
    return render(request, 'index.html', context)

    
class search(TemplateView):
   template_name = 'search.html'
   