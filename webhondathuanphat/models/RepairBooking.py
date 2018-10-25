from django.db import models
from django.contrib.auth.models import User

CONST = {
    #'userp': 'Khách hàng',
    'cname': 'Tên thường gọi',
    'phone': 'Số điện thoại',
    'model': 'Loại xe',
    'datep': 'Ngày hẹn',
    'timep': 'Giờ hẹn',
    'sympt': 'Hiện tượng',
    'partl': 'Phụ tùng',
    'confm': 'Xác nhận',
    'notep': 'Ghi chú',
}

class RepairBooking(models.Model):
    #userp = models.ForeignKey(User, on_delete=models.PROTECT)
    cname = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    model = models.CharField(max_length=20)
    datep = models.CharField(max_length=20)
    timep = models.CharField(max_length=10)
    sympt = models.TextField(blank=True)
    partl = models.TextField(blank=True)
    confm = models.BooleanField(default=False)
    notep = models.TextField(blank=True)
    isD = models.BooleanField(default=False)

    class Meta:
        db_table = "RepairBooking"
