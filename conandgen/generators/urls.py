from django.urls import path
from . import views

app_name = 'generators'

urlpatterns = [
    
    path('',views.gensis, name = 'gensis'),
    path('password/',views.password,name='password'),
   
    
    
]
