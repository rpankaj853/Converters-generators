"""conandgen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from convertors import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('convert',views.convert, name = 'convert'),
    path('generators/', include('generators.urls')),
    path('textcon',views.textcon, name = 'textcon'),
    path('currencycon/',views.currencycon, name = 'currencycon'),
    path('markscon/',views.markscon, name = 'markscon'),
    path('fileconvert/',views.fileconvert, name = 'fileconvert'),
    path('thermocon/',views.thermocon, name = 'thermocon'),
    path('cryptocon/',views.cryptocon, name = 'cryptocon'),
    
]
