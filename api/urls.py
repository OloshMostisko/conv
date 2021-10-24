from django.urls import path

from api import views 
from . views import *
app_name = "api"

urlpatterns = [
    path('', views.index, name='index'),

    path('search/', views.search.as_view(), name = 'search'),
    path('search_result/', views.searchResult.as_view(template_name = 'srcResut.html'), name= 'search_result'),


    path('reg/<int:s_id>/<str:std_full_name>/', PaymentView.as_view(), name='reg'),
    path('payment', PayView, name='payment'),
    path('success', CheckoutSuccessView.as_view(), name='success'),
    path('faild', CheckoutFaildView.as_view(), name='faild'),



    path('first', views.c_first, name='c_first'),
    path('second', views.c_second, name='c_second'),
    path('third', views.c_third, name='c_third'),
    path('fourth', views.c_fourth, name='c_fourth'),
    path('committees', views.committees, name='committees'),
    path('confirmation/<s_id>/<name>/', views.confirmation, name='confirmation'),
    path('contact', views.contact, name='contact'),
    path('edit', views.edit, name='edit'),
    path('eligible', views.eligible, name='eligible'),
    path('galarry', views.gallery, name='gallery'),
    path('goldmedels', views.goldmadelists, name='goldmadelists'),
   # path('payment', views.payment, name='payment'),
    path('registration', views.registration, name='registration'),
    path('rules', views.rules, name='rules'),
    path('schedule', views.schedule, name='schedule'),
    path('sp_details', views.speech_detail, name='speech_detail'),
    path('speech', views.speech, name='speech'),
    path('venu', views.venu, name='venu'),

]