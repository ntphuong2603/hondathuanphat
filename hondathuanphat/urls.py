"""hondathuanphat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('webhondathuanphat.urls')),
    path('', include('webhondathuanphat.urls_0')),
    path('', include('webhondathuanphat.urlsAjaxFunction')),
    path('banhang/', include('webhondathuanphat.urlsBanhang')),
    path('dichvu/', include('webhondathuanphat.urlsDichvu')),
    #path('phutung/', include('webhondathuanphat.urlsPhutung')),
    #path('laixeAntoan/', include('webhondathuanphat.urlsLaixeAntoan')),
    #path('tintuc/', include('webhondathuanphat.urlsTintuc')),
    #path('tuyendung/', include('webhondathuanphat.urlsTuyendung')),
    path('nhanvien/', include('webhondathuanphat.urlsNhanvien')),
    path('thanhvien/', include('webhondathuanphat.urlsThanhvien')),
]
