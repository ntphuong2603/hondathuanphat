from django.db import models
from django.contrib.auth.models import User
from . import dbFunctions as functions

CONST = {
    'phn': 'Số điện thoại',
    'add': 'Địa chỉ',
    'nme': 'Tên thường gọi',
    'ava': 'Ảnh đại diện',
    'fnm': 'Tên',
    'lnm': 'Họ',
    'ema': 'Địa chỉ email',
    'dte': 'Ngày gia nhập',
}

class Member(models.Model):
    usr = models.OneToOneField(User, on_delete=models.PROTECT)
    add = models.TextField(blank=True)
    phn = models.CharField(blank=True, max_length=12)
    nme = models.CharField(blank=True, max_length=100)
    ava = models.CharField(blank=True, max_length=100)
    isD = models.BooleanField(default=False)

    def getMember(self, user_id):
        mbr = Member.objects.filter(usr_id=user_id).values()
        usr = User.objects.filter(id=user_id).values()
        rlt = functions.makeDict(mbr, {}, CONST)
        rlt = functions.makeDict(usr, rlt, CONST)
        return rlt

    class Meta:
        db_table = "Member"
