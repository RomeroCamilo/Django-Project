from django.urls import path
from . import views


#URL Configuration.
#For each function made in views, add a path/url to run to a specific function.
urlpatterns = [
    path('camilo/', views.personal_page),
    path('family/', views.family_members),
]