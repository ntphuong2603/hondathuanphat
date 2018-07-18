from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Member
from datetime import date
from .pyFolder.baseMenu import NHAN_VIEN, webParam, WEB_DATA
from .pyFolder.navMenu import pageReturn


def dangnhap(request):
    if request.method == 'POST':
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')
        try:
            userLogin = authenticate(username=usr, password=pwd)
            login(request, userLogin)
            if userLogin.is_active and userLogin.is_staff:
                data = {'login':'OK'}
            else:
                data = {'login':'NG'}
        except Exception as e:
            data = {'login':'NG'}
        return JsonResponse(data)
    else:
        pageReturn(request, NHAN_VIEN)



def dangxuat(request):
    if request.method == 'POST':
        logout(request)
        data = {'logout' : 'OK'}
        return JsonResponse(data)


@login_required(login_url='dangnhap')
def capnhatthongtincanhan(request):
    return capnhatthongtin(request=request)


@login_required(login_url='dangnhap')
def capnhatmatkhau(request):
    return capnhatthongtin(request=request, isPass=True)


@login_required(login_url='dangnhap')
def thongtincanhan(request):
    webParam['webData'] = Member().getMember(request.user.id)
    return pageReturn(request, THANH_VIEN)


def capnhatthongtin(request, isPass = False):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        commentName = request.POST.get('commentName')
        avatar = ''
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        try:
            usr = User.objects.get(username=request.user)
            mem = Member.objects.get(user_id=usr.id)
            mem.update()
            usr.update()
            usr.save()
            mem.save()
            if isPass:
                pwd = request.POST.get('password')
                usr.set_password(pwd)
            data = {'update':'OK'}
        except Exception as e:
            data = {'update':'NG'}
    return JsonResponse(data)
