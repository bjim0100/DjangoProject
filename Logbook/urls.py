from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.Home, name= 'home'),
    path('log/', views.Login, name= 'logstaff'),
    path('visitor/', views.Visitor, name = 'visitor')
]