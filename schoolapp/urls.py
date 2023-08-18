from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("login/",views.loginPage,name='login'),
    path("register/",views.registerPage,name='register'),
    path("add/",views.studentform,name='student-reg'),
    path("logout/",views.logoutUser,name='logout'),
    path("new/",views.new,name='new'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]
