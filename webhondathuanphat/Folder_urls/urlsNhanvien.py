from django.urls import path
from ..Folder_views import viewsNhanvien as nhanvien
from ..views import thongtincanhan


urlpatterns = [
    path('xemlichhensuachua', nhanvien.xemlichhensuachua, name='xemlichhensuachua'),
    path('loaixe', nhanvien.loaixe, name='loaixe'),
    path('thongtincanhan', thongtincanhan, name='thongtinnhanvien'),
    path('xemlichsusuachua', nhanvien.xemlichsusuachua, name='xemlichsusuachua'),
    path('danhsachxedangsuachua', nhanvien.danhsachxedangsuachua, name='danhsachxedangsuachua'),
]
