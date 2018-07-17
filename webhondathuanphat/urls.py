from django.urls import path
from django.conf.urls import url
from . import views, viewsBanhang as banhang, viewsDichvu as dichvu, viewsThanhvien as thanhvien


urlpatterns = [
    path('', views.trangchu, name='trangchu'),
    #viewsBanhang
    path('banhang/theoLoaiXe/<int:loaiXe>', banhang.theoLoaiXe, name='theoLoaiXe'),
    #viewsDichvu
    path('dichvu/hensuachua', dichvu.henlichsuachua, name='henlichsuachua'),
    #viewsThanhvien
    path('thanhvien/dangky', thanhvien.dangky, name='dangky'),
    path('thanhvien/dangnhap', thanhvien.dangnhap, name='dangnhap'),
    path('thanhvien/thongtincanhan', thanhvien.thongtincanhan, name='thongtincanhan'),
    path('thanhvien/dangxuat', thanhvien.dangxuat, name='dangxuat'),
    #views
	path('phutung', views.phutung, name='phutung'),
	path('laixeantoan', views.laixeantoan, name='laixeantoan'),
	path('tintuc', views.tintuc, name='tintuc'),
	path('tuyendung', views.tuyendung, name='tuyendung'),
    #ajax functions for thanhvien
    url(r'^ajax/thanhvien/dangnhap$', thanhvien.dangnhap),
	url(r'^ajax/thanhvien/kiemtraTendangnhap$', thanhvien.kiemtraTendangnhap),
	url(r'^ajax/thanhvien/thanhvienDangxuat$', thanhvien.thanhvienDangxuat),
	url(r'^ajax/thanhvien/capnhatthongtincanhan$', thanhvien.capnhatthongtincanhan),
	url(r'^ajax/thanhvien/capnhatmatkhau$', thanhvien.capnhatmatkhau),
    #ajax functions for dichvu
    url(r'^ajax/dichvu/dangkyLichhen$', dichvu.henlichsuachua),
    #ajax functions for nhanvien
    #url(r'^ajax/nhanvien/dangnhap$', nhanvien.nhanvienDangnhap),
    #url(r'^ajax/nhanvien/changeBookingStatus$', nhanvien.thanhdoiTrangthaiBooking),
]
