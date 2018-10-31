from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
#from ..models import Member
from ..models import dbFunctions as functions
from datetime import date
from ..Folder_pyFile.baseMenu import THANH_VIEN, webParam, WEB_DATA
from ..Folder_pyFile.navMenu import pageReturn


def dangnhap(request):
    return pageReturn(request, THANH_VIEN)


def dangxuat(request):
    return pageReturn(request, THANH_VIEN)


def dangky(request):
    if request.method == 'POST':
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')
        return JsonResponse({"result" : functions.getUser(usr, pwd)})
    return pageReturn(request, THANH_VIEN)


@login_required(login_url='dangnhap')
def thongtinxe(request):
    return pageReturn(request, THANH_VIEN)


@login_required(login_url='dangnhap')
def capnhatmatkhau(request):
    return None


@login_required(login_url='dangnhap')
def getModelList(request):
    return None


@login_required(login_url='dangnhap')
def getModelHistory(request):
    return None
