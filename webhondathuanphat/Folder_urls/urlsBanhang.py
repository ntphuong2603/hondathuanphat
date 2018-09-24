from django.urls import path
from ..Folder_views import viewsBanhang as banhang


urlpatterns = [
    path('theoLoaixe/<int:loaiXe>', banhang.theoLoaixe, name='theoLoaixe'),
    path('theoDoixe/<str:doiXe>', banhang.theoDoixe, name='theoDoixe'),
]
