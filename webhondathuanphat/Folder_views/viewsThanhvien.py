from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from ..models import Member
from datetime import date
from ..Folder_pyFile.baseMenu import THANH_VIEN, webParam, WEB_DATA
from ..Folder_pyFile.navMenu import pageReturn


def dangnhap(request):
    return pageReturn(request, THANH_VIEN)


def dangxuat(request):
    return pageReturn(request, THANH_VIEN)


def dangky(request):
    if request.method == 'POST':
        data = {'user' : 'NG'}
        usr = request.POST.get('usr')
        if not User.objects.filter(username=usr).exists():
            user = User(username=usr, email='')
            user.set_password(request.POST.get('pwd'))
            user.save()
            data = {'user':'OK'}
        return JsonResponse(data)
    return pageReturn(request, THANH_VIEN)


@login_required(login_url='dangnhap')
def thongtinxe(request):
    return pageReturn(request, THANH_VIEN)


@login_required(login_url='dangnhap')
def capnhatmatkhau(request):
    return capnhatthongtin(request=request, isPass=True)

@login_required(login_url='dangnhap')
def getModelList(request):
    return None

@login_required(login_url='dangnhap')
def getModelHistory(request):
    return None
