
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index,name='homes'),
    path("signup", views.signup,name='signup'),
    path("login", views.login,name='login'),
    path("contact", views.contact,name='contact'),
]