from django.urls import path

from api import views 
app_name = "api"

urlpatterns = [
    path('', views.index, name='index'),

    path('search', views.search.as_view(), name= 'search'),
    path('search_result', views.searchResult.as_view(), name= 'search_result'),

    path('search', views.search.as_view(), name= "search"),

    path('first', views.c_first, name='c_first'),
    path('second', views.c_second, name='c_second'),
    path('third', views.c_third, name='c_third'),
    path('fourth', views.c_fourth, name='c_fourth'),
    path('committees', views.committees, name='committees'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('contact', views.contact, name='contact'),
    path('edit', views.edit, name='edit'),
    path('eligible', views.eligible, name='eligible'),
    path('galarry', views.gallery, name='gallery'),
    path('goldmedels', views.goldmadelists, name='goldmadelists'),
    path('payment', views.payment, name='payment'),
    path('registration', views.registration, name='registration'),
    path('rules', views.rules, name='rules'),
    path('schedule', views.schedule, name='schedule'),
    path('sp_details', views.speech_detail, name='speech_detail'),
    path('speech', views.speech, name='speech'),
    path('venu', views.venu, name='venu'),

]