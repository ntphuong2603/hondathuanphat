from django.conf.urls import url
from . import views
from . import viewsBanhang as banhang, viewsDichvu as dichvu, viewsThanhvien as thanhvien, viewsNhanvien as nhanvien


urlpatterns = [
    url(r'^ajax/thanhvien/dangnhap$', views.thanhvienDangnhap),
    url(r'^ajax/nhanvien/dangnhap$', views.nhanvienDangnhap),
    url(r'^ajax/capnhatthongtin$', views.thongtincanhan),
    url(r'^ajax/dangxuat$', views.dangxuat),
	#url(r'^ajax/thanhvien/kiemtraTendangnhap$', thanhvien.kiemtraTendangnhap),
	url(r'^ajax/capnhatmatkhau$', thanhvien.capnhatmatkhau),
    #ajax functions for dichvu
    url(r'^ajax/dichvu/dangkyLichhen$', dichvu.henlichsuachua),
    #ajax functions for nhanvien
    url(r'^ajax/nhanvien/changeBookingStatus$', nhanvien.thaydoiTrangthaiBooking),
]
