from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Member
from datetime import date
from .pyFolder.baseMenu import THANH_VIEN, webParam, WEB_DATA
from .pyFolder.navMenu import pageReturn


def dangnhap(request):
    return pageReturn(request, THANH_VIEN)


def dangxuat(request):
    return pageReturn(request, THANH_VIEN)


def dangky(request):
    if request.method == 'POST':
        return thanhvien(request)
    return pageReturn(request, THANH_VIEN)


def kiemtraTendangnhap(request):
    #print(request)
    if request.method == "POST":
        usr = request.POST.get('usr')
        data = {'user' : 'OK'}
        try:
            user = User.objects.get(username=usr)
        except User.DoesNotExist:
            data['user'] = 'NG'
        finally:
            #print(data)
            return JsonResponse(data)


@login_required(login_url='dangnhap')
def thongtinxe(request):
    return pageReturn(request, THANH_VIEN)


@login_required(login_url='dangnhap')
def capnhatmatkhau(request):
    return capnhatthongtin(request=request, isPass=True)
