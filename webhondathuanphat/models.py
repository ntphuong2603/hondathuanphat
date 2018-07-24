from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class ProductCaterogy(models.Model):
    name = models.CharField("Loại xe", max_length=30)
    class Meta:
        db_table = "Caterogy"


class RepairBooking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    model = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    symptom = models.TextField(blank=True)
    partList = models.TextField(blank=True)
    confirm = models.BooleanField(default=False)
    note = models.TextField(blank=True)
    class Meta:
        db_table = "RepairBooking"


def makeDict(querySet, result, className):
    for eachIterator in querySet.iterator():
        for eachKey in eachIterator.keys():
            if eachKey in className.keys():
                strList = [className[eachKey], eachIterator[eachKey]]
                result[eachKey] = strList
    print(result)
    return result


# Create your models here.
class Member(models.Model):
    MEMBER = {
        'phone' : 'Số điện thoại',
        'address': 'Địa chỉ',
        'commentName': 'Tên thường gọi',
        'avatar' : 'Ảnh đại diện',
        'first_name': 'Tên',
        'last_name' : 'Họ',
        'email' : 'Địa chỉ email',
        'date_jointed': 'Ngày gia nhập',
        'username': 'Tên đăng nhập'
    }

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=12, blank=True)
    address = models.TextField(blank=True)
    commentName = models.CharField(blank=True, max_length=100)
    avatar = models.CharField(blank=True, max_length=100)

    def getMember(self, user_id):
        member = Member.objects.filter(user_id=user_id).values()
        user = User.objects.filter(id=user_id).values()
        print("Member: ", member)
        print("User: ", user)
        result = makeDict(member,{}, self.MEMBER)
        result = makeDict(user, result, self.MEMBER)
        return result

    class Meta:
        db_table = "Member"
