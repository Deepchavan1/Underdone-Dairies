from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('postComment', views.postComment, name="postComment"),
  
  path('', views.poemHome, name='poemHome'),
  path('<str:slug>', views.poemPost, name='views.poemPost'),
]