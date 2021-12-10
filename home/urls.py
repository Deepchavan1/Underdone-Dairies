from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
  path('', views.home, name='home'),
  path('logout', views.handelLogout, name="handleLogout"),
  path('signup', views.handleSignUp, name="signup"),
  path('login', views.handeLogin, name="handleLogin"),
  path('contact/', views.contact, name="ContactUs"),
]