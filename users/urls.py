from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('accounts/', views.login_user, name='accounts'),
    path('logout/', views.logout_user, name='logout'),
  #  path('editprofile/', views.edit_profile, name='eidtprofile'),
    path('profile/', views.user_profile, name='profile'),
    
]