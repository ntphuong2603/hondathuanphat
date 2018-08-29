from django.urls import path
from . import viewsNhanvien as nhanvien


urlpatterns = [
    path('xemlichhensuachua', nhanvien.xemlichhensuachua, name='xemlichhensuachua'),
    path('loaixe', nhanvien.loaixe, name='loaixe'),
]
