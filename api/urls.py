from django.urls import path

from api import views 
from . views import *
app_name = "api"

urlpatterns = [
    path('', views.index, name='index'),

    path('search/', views.search.as_view(), name = 'search'),
    path('search_result/', views.searchResult.as_view(template_name = 'search/srcResut.html'), name= 'search_result'),


    path('reg/<s_id>/<std_full_name>/', PaymentView.as_view(), name='reg'),
    path('payment', PayView, name='payment'),
    
    #for accounce with login
    path('search2/', views.search2.as_view(), name = 'search2'),
    path('search_result2/', views.searchResult2.as_view(template_name = 'search/srcResut2.html'), name= 'search_result2'),

    path('reg2/<s_id>/<std_full_name>/', PaymentView2.as_view(), name='reg2'),
    path('payment2', PayView2, name='payment2'),

    path('success', CheckoutSuccessView.as_view(), name='success'),
    path('faild', CheckoutFaildView.as_view(), name='faild'),

    path('paysearch/', views.PaymentSearch.as_view(), name = 'paysearch'),
    path('paySearchresult/', views.PaySearchResultView.as_view(template_name = 'reg/paySrcResult.html'), name= 'paySearchresult'),
    
    # path('confirm/<sid>/<name>/<email>/', views.ConfirmationView.as_view(), name='confirm'),
    #path('confirmdone', Confirmation, name='confirmdone'),

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

    # path('registration', views.registration, name='registration'),
    # path('registration2', views.registration2, name='registration2'),
    path('rules', views.rules, name='rules'),
    path('schedule', views.schedule, name='schedule'),
    path('sp_details', views.speech_detail, name='speech_detail'),
    path('speech', views.speech, name='speech'),
    path('venu', views.venu, name='venu'),

]