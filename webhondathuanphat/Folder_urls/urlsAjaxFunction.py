from django.conf.urls import url
from .. import views
from ..Folder_views import viewsBanhang as banhang, viewsDichvu as dichvu, viewsThanhvien as thanhvien, viewsNhanvien as nhanvien


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
    url(r'^ajax/nhanvien/showBooking_notConfirm$', nhanvien.showBooking_notConfirm),
    url(r'^ajax/nhanvien/showBooking_all$', nhanvien.showBooking_all),
    url(r'^ajax/nhanvien/showBooking_confirmed$', nhanvien.showBooking_confirmed),
    url(r'^ajax/nhanvien/getListThanhvien$', nhanvien.getListThanhvien),
    url(r'^ajax/nhanvien/xemLichsuSudungDichvu$', nhanvien.xemLichsuSudungDichvu),
    url(r'^ajax/nhanvien/themxevaotram$', nhanvien.themxevaotram),
    url(r'^ajax/nhanvien/thanhtoantienDichvu$', nhanvien.thanhtoantienDichvu),
    url(r'^ajax/nhanvien/getPhoneBookingList$', nhanvien.getPhoneBookingList),
]
