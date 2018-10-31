from django.db import models
from django.contrib.auth.models import User

CONST = {
    'phn': 'Số điện thoại',
    'add': 'Địa chỉ',
    'nme': 'Tên thường gọi',
    #'ava': 'Ảnh đại diện',
    #'isD': 'Đã xóa'
}

class Member(models.Model):
    usr = models.OneToOneField(User, on_delete=models.PROTECT)
    add = models.TextField(blank=True)
    phn = models.CharField(blank=True, max_length=12)
    nme = models.CharField(blank=True, max_length=100)
    ava = models.CharField(blank=True, max_length=100)
    isD = models.BooleanField(default=False)

    class Meta:
        db_table = "Member"
