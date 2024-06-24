from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('signup/',views.user_signup,name='blog-signup'),
    path('login/',views.user_login,name='blog-login'),
    path('Logout', views.user_logout, name='Logout'),
    path('about', views.user_about, name='blog-About'),
    
    

    # Add more paths as needed
]