from django.urls import path
from django.conf.urls import url
from . import views, viewsBanhang as banhang, viewsDichvu as dichvu, viewsThanhvien as thanhvien, viewsNhanvien as nhanvien


urlpatterns = [
    #views
    path('', views.trangchu, name='trangchu'),
	path('phutung', views.phutung, name='phutung'),
	path('laixeantoan', views.laixeantoan, name='laixeantoan'),
	path('tintuc', views.tintuc, name='tintuc'),
	path('tuyendung', views.tuyendung, name='tuyendung'),
    path('thanhvien/thongtincanhan', views.thongtincanhan, name='thongtinthanhvien'),
    path('nhanvien/thongtincanhan', views.thongtincanhan, name='thongtinnhanvien'),
    #viewsBanhang
    path('banhang/theoLoaiXe/<int:loaiXe>', banhang.theoLoaiXe, name='theoLoaiXe'),
    #viewsDichvu
    path('dichvu/hensuachua', dichvu.henlichsuachua, name='henlichsuachua'),
    #viewsThanhvien
    path('thanhvien/dangky', thanhvien.dangky, name='dangky'),
    path('thanhvien/dangnhap', thanhvien.dangnhap, name='dangnhap'),
    path('thanhvien/thongtinxe', thanhvien.thongtinxe, name='thongtinxe'),
    #viewsNhanvien
    path('nhanvien/xemlichhensuachua', nhanvien.xemlichhensuachua, name='xemlichhensuachua'),
    path('nhanvien/loaixe', nhanvien.loaixe, name='loaixe'),
    #ajax functions for thanhvien
    url(r'^ajax/thanhvien/dangnhap$', views.thanhvienDangnhap),
    url(r'^ajax/nhanvien/dangnhap$', views.nhanvienDangnhap),
    url(r'^ajax/capnhatthongtin$', views.thongtincanhan),
    url(r'^ajax/dangxuat$', views.dangxuat),
	url(r'^ajax/thanhvien/kiemtraTendangnhap$', thanhvien.kiemtraTendangnhap),
	url(r'^ajax/capnhatmatkhau$', thanhvien.capnhatmatkhau),
    #ajax functions for dichvu
    url(r'^ajax/dichvu/dangkyLichhen$', dichvu.henlichsuachua),
    #ajax functions for nhanvien
    url(r'^ajax/nhanvien/changeBookingStatus$', nhanvien.thaydoiTrangthaiBooking),
]
