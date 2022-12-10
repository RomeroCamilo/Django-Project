#Purpose of this file: This file will be used to add url configurations to any function you would like to exectute/render from the views.py file in your app.

from django.urls import path
from . import views


#URL Configuration.
#For each function made in views, add a path/url to run to a specific function. Try to make url name relevant.
urlpatterns = [
    #path to my personal html page.
    path('camilo/', views.personal_page),
    #path to a function that will print data from mysql.
    path('family/', views.family_members),
]