from django.urls import path
from ..Folder_views import viewsThanhvien as thanhvien
from ..views import thongtincanhan


urlpatterns = [
    path('dangky', thanhvien.dangky, name='dangky'),
    path('dangnhap', thanhvien.dangnhap, name='dangnhap'),
    path('thongtinxe', thanhvien.thongtinxe, name='thongtinxe'),
    path('thongtincanhan', thongtincanhan, name='thongtinthanhvien'),
]
