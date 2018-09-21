import datetime, time, json
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Member
from .models import RepairBooking
from .pyFolder.baseMenu import DICH_VU, NHAN_VIEN, webParam, WEB_DATA
from .pyFolder.navMenu import pageReturn
from .pyFolder import jsonFile

HISTORY_FOLDER = 'webhondathuanphat\\jsonFolder\\history\\'

@login_required(login_url='dangnhap')
def xemlichhensuachua(request):
    return pageReturn(request, DICH_VU)


@login_required(login_url='dangnhap')
def loaixe(request):
    return pageReturn(request, DICH_VU)


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

@login_required(login_url='dangnhap')
def xemlichsusuachua(request):
    return pageReturn(request, DICH_VU)

@login_required(login_url='dangnhap')
def getListThanhvien(request):
    if request.method == 'POST':
        data = {'listThanhvien': []}
        all_User = User.objects.all().filter(is_active=True, is_superuser=False)
        for eachIterator in list(all_User.values()):
            data['listThanhvien'].append(eachIterator['username'])
        return JsonResponse(data)

def getHistory(data):
    keyList = ['plateNumber', 'modelName', 'mileage', 'amount', 'service', 'mech']
    result = {}
    for each in sorted(data.keys(), reverse=True):
        day = datetime.datetime.utcfromtimestamp(int(each)).strftime("%d-%m-%Y")
        timein = datetime.datetime.utcfromtimestamp(int(each)).strftime("%H:%M")
        timeout = datetime.datetime.utcfromtimestamp(int(data[each]['finish'])).strftime("%H:%M")
        result[day] = { 'timein': timein, 'timeout': timeout}
        for eachKey in keyList:
            result[day][eachKey] = data[each][eachKey]
    return result

@login_required(login_url='dangnhap')
def xemLichsuSudungDichvu(request):
    if request.method == 'POST':
        data = {'summary': {}, 'history': {}, 'using': {}}
        dataHistory = jsonFile.readFile(pathFile = HISTORY_FOLDER, fileName = request.POST.get('usr'))
        if dataHistory is not None:
            data = {'summary': dataHistory['summary'],
                    'history': getHistory(dataHistory['earning']),
                    'using': getHistory(dataHistory['spending'])}
        return JsonResponse(data)

@login_required(login_url='dangnhap')
def danhsachxedangsuachua(request):
    file_DanhsachXeDangSuaChua = 'xeDangSuaChua'
    data = {'danhsachXe': jsonFile.readFile(pathFile = HISTORY_FOLDER, fileName = file_DanhsachXeDangSuaChua)}
    #return JsonResponse(data)
    #webParam[WEB_DATA] = jsonFile.readFile(pathFile = HISTORY_FOLDER, fileName = file_DanhsachXeDangSuaChua)
    return pageReturn(request, DICH_VU)
