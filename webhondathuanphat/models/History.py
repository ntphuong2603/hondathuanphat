import time
from django.db import models
from django.contrib.auth.models import User
from . import dbFunctions as functions

CONST = {
    "usr": "Khách hàng",
    "mod": "Loại xe",
    "mil": "Số km",
    "ser": "Công việc",
    "mec": "Tên thợ",
    "amt": "Thành tiền",
    "din": "Giờ vào",
    "dot": "Giờ ra",
    "isF": "Tình trạng",
    "isD": "Đã xóa"
}

class History(models.Model):
    usr = models.ForeignKey(User, on_delete=models.PROTECT)
    mod = models.CharField(max_length=30, blank=True)
    mil = models.CharField(max_length=30, blank=True)
    ser = models.CharField(max_length=30, blank=True)
    mec = models.CharField(max_length=30, blank=True)
    amt = models.CharField(max_length=30, default="0")
    din = models.CharField(max_length=30, blank=True)
    dot = models.CharField(max_length=30, blank=True)
    isF = models.BooleanField(default=False)
    isD = models.BooleanField(default=False)

    class Meta:
        db_table = "History"
