from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_user, name='login'),
 #   path('logout/', views.logout_user, name='logout'),
  #  path('editprofile/', views.edit_profile, name='eidtprofile'),
    path('profile/', views.user_profile, name='profile'),
    
]