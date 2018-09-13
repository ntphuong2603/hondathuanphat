from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Member
from .models import RepairBooking
from .pyFolder.baseMenu import DICH_VU, NHAN_VIEN, webParam, WEB_DATA
from .pyFolder.navMenu import pageReturn


@login_required(login_url='dangnhap')
def xemlichhensuachua(request):
    return pageReturn(request, DICH_VU)


@login_required(login_url='dangnhap')
def loaixe(request):
    return pageReturn(request, NHAN_VIEN)


@login_required(login_url='dangnhap')
def thaydoiTrangthaiBooking(request):
    if request.method == 'POST':
        data = {'update':'OK'}
        #confirmList = request.POST.get('confirmList').split(',')
        #print(confirmList)
        #booking_ID = int(request.POST.get('id'))
        for each in request.POST.get('confirmList').split(','):
        #for each in confirmList:
            booking = RepairBooking.objects.get(id=each)
            booking.confirm = True
            booking.save()
        return JsonResponse(data)

def getBooking(confirmStatus=None):
    if (confirmStatus is None):
        all_booking = RepairBooking.objects.all()
    else:
        all_booking = RepairBooking.objects.all().filter(confirm=confirmStatus)
    result = {}
    for eachIterator in list(all_booking.values()):
        result[eachIterator['id']]=eachIterator
    return render_to_response('table_0.html', {'result': result})

@login_required(login_url='dangnhap')
def showBooking_all(request):
    return getBooking()

@login_required(login_url='dangnhap')
def showBooking_notConfirm(request):
    return getBooking(False)

@login_required(login_url='dangnhap')
def showBooking_confirmed(request):
    return getBooking(True)
