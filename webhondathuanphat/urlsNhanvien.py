from django.urls import path
from . import viewsNhanvien as nhanvien
from .views import thongtincanhan


urlpatterns = [
    path('xemlichhensuachua', nhanvien.xemlichhensuachua, name='xemlichhensuachua'),
    path('loaixe', nhanvien.loaixe, name='loaixe'),
    path('thongtincanhan', thongtincanhan, name='thongtinnhanvien'),
]
