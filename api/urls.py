from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.c_first, name='c_first'),
    path('', views.c_second, name='c_second'),
    path('', views.c_third, name='c_third'),
    path('', views.c_fourth, name='c_fourth'),
    path('', views.committees, name='committees'),
    path('', views.confirmation, name='confirmation'),
    path('', views.contact, name='contact'),
    path('', views.edit, name='edit'),
    path('', views.eligible, name='eligible'),
    path('', views.gallery, name='gallery'),
    path('', views.goldmadelists, name='goldmadelists'),
    path('', views.payment, name='payment'),
    path('', views.registration, name='registration'),
    path('', views.rules, name='rules'),
    path('', views.schedule, name='schedule'),
    path('', views.speech_detail, name='speech_detail'),
    path('', views.speech, name='speech'),
    path('', views.venu, name='venu'),
]