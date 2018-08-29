from django.urls import path
from . import viewsThanhvien as thanhvien


urlpatterns = [
    path('dangky', thanhvien.dangky, name='dangky'),
    path('dangnhap', thanhvien.dangnhap, name='dangnhap'),
    path('thongtinxe', thanhvien.thongtinxe, name='thongtinxe'),
]
