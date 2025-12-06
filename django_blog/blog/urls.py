from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path("", views.signup, name="signup"), 
    path('home/', views.home, name='home'),
    path('newpost/', views.newPost, name='newPost'),
    path('mypost/', views.myPosts, name='myPosts'),
    path('signout/', views.signOut, name='signout'),
]