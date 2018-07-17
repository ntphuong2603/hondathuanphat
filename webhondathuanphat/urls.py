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
    #views
	path('phutung', views.phutung, name='phutung'),
	path('laixeantoan', views.laixeantoan, name='laixeantoan'),
	path('tintuc', views.tintuc, name='tintuc'),
	path('tuyendung', views.tuyendung, name='tuyendung'),
]
