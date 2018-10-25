import datetime, time, json
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import dbFunctions as functions
from ..models.Member import Member
from ..models.RepairBooking import RepairBooking, CONST as CONST_Rep
from ..models.History import History, CONST as CONST_His
from ..Folder_pyFile.baseMenu import DICH_VU, NHAN_VIEN, webParam, WEB_DATA
from ..Folder_pyFile.navMenu import pageReturn


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
        for each in request.POST.get('confirmList').split(','):
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
        dataHistory = functions.getAll(History, CONST_His, {'usr_id': functions.getUser(request.POST.get('usr')).id})
        print(dataHistory)
        if dataHistory is not None:
            data = {'summary': dataHistory['summary'],
                    'history': getHistory(dataHistory['earning']),
                    'using': getHistory(dataHistory['spending'])}
        return JsonResponse(data)


@login_required(login_url='dangnhap')
def danhsachxedangsuachua(request):
    history = functions.getAll(History, CONST_His, {'isF':False})
    print(history)
    webParam[WEB_DATA] = {'danhsachXe': history, 'number': len(history)}
    return pageReturn(request, DICH_VU)


@login_required(login_url='dangnhap')
def themxevaotram(request):
    if request.method == 'POST':
        dataDict = {}
        for each in CONST_His.keys():
            value = request.POST.get(each)
            if not value is None:
                dataDict[each] = value
        print(dataDict)
        #dataDict['din'] = int(time.time())
        dataDict['din'] = datetime.datetime.fromtimestamp(int(time.time())).strftime("%d-%m-%Y - %H:%M")
        history = functions.createObject(History, dataDict, request.POST.get('pho'))
        data = functions.queryTOdict(functions.getObject(History, history.id).values(), CONST_His)
        #print(data)
        return render_to_response('themxedangsuachua.html', {'danhsachXe': data})


@login_required(login_url='dangnhap')
def thanhtoantienDichvu(request):
    if request.method == 'POST':
        result = {'result': 'OK'}
        return JsonResponse(result)


@login_required(login_url='dangnhap')
def getPhoneBookingList(request):
    if request.method == 'POST':
        today = datetime.datetime.utcfromtimestamp(time.time()).strftime("%d-%m-%Y")
        bookingDict = functions.getAll(RepairBooking, CONST_Rep, {"confm": True, "datep": today})
        #print("No: ", len(bookingDict), "Bookings: ", bookingDict.keys())
        listPhoneBooking = []
        data = {}
        for eachBookingID in bookingDict.keys():
            oneBooking = bookingDict[eachBookingID]
            #print("One-Booking: ", oneBooking)
            listPhoneBooking.append(oneBooking['phone'][1])
            subData = {}
            for each in CONST_His.keys():
                if each in oneBooking.keys():
                    subData[each] = oneBooking[each][1]
                else:
                    subData[each] = ""
            subData['cus'] = oneBooking['cname'][1]
            subData['din'] = datetime.datetime.utcfromtimestamp(int(time.time())).strftime("%d-%m-%y lúc %H:%M")
            subData['amt'] = "0"
            subData['mec'] = ""
            data[eachBookingID] = subData
        #print(listPhoneBooking)
        #print(data)
        return JsonResponse({'listPhoneBooking':listPhoneBooking, 'bookingDetail': data})
