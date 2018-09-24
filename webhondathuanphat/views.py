from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Member
from .Folder_pyFile.baseMenu import TRANG_CHU, BAN_HANG, DICH_VU, PHU_TUNG, LAI_XE_AN_TOAN, THANH_VIEN, TIN_TUC, TUYEN_DUNG, NHAN_VIEN
from .Folder_pyFile.navMenu import pageReturn, webParam


# Create your views here.
def trangchu(request):
    return pageReturn(request, TRANG_CHU)


def banhang(request):
    return pageReturn(request, BAN_HANG)


def dichvu(request):
    return pageReturn(request, DICH_VU)


def phutung(request):
    return pageReturn(request, PHU_TUNG)


def laixeantoan(request):
    return pageReturn(request, LAI_XE_AN_TOAN)


def thanhvien(request):
    return pageReturn(request, THANH_VIEN)


def tintuc(request):
    return pageReturn(request, TIN_TUC)


def tuyendung(request):
    return pageReturn(request, TUYEN_DUNG)


def thanhvienDangnhap(request):
    if request.method == 'POST':
        #print(request)
        return dangnhap(request, is_staff=False)


def nhanvienDangnhap(request):
    if request.method == 'POST':
        #print(request)
        return dangnhap(request, is_staff=True)


def dangnhap(request, is_staff):
    try:
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')
        userLogin = authenticate(username=usr, password=pwd)
        login(request, userLogin)
        #print(not is_staff, userLogin.is_active)
        #print(is_staff, userLogin.is_staff)
        #print(request)
        if (not is_staff and userLogin.is_active) or (is_staff and userLogin.is_staff):
            data = {'login':'OK'}
        else:
            logout(request)
            data = {'login':'NG'}
    except Exception as e:
        data = {'login':'NG'}
    return JsonResponse(data)


def dangxuat(request):
    if request.method == 'POST':
        logout(request)
        data = {'logout' : 'OK'}
        return JsonResponse(data)


@login_required(login_url='dangnhap')
def thongtincanhan(request):
    if request.method == 'POST'  :
        return capnhatthongtin(request, isPass = False)
    else:
        webParam['webData'] = Member().getMember(request.user.id)
        if request.user.is_staff:
            return pageReturn(request, NHAN_VIEN)
        else:
            return pageReturn(request, THANH_VIEN)


@login_required(login_url='dangnhap')
def capnhatmatkhau(request):
    if request.method == 'POST':
        return capnhatthongtin(request, isPass = True)


def capnhatthongtin(request, isPass = False):
    try:
        usr = User.objects.get(username=request.user)
        usr.first_name = request.POST.get('first_name')
        usr.last_name = request.POST.get('last_name')
        usr.email = request.POST.get('email')
        usr.save()
        mem = Member.objects.get(user_id=usr.id)
        mem.phone = request.POST.get('phone')
        mem.address = request.POST.get('address')
        mem.commentName = request.POST.get('commentName')
        mem.save()
        if isPass:
            pwd = request.POST.get('password')
            usr.set_password(pwd)
        data = {'update':'OK'}
    except Exception as e:
        data = {'update':'NG'}
    return JsonResponse(data)
