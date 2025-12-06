from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path("", views.signup, name="signup"), 
    path('home/', views.home, name='home'),
]