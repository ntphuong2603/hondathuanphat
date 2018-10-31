import datetime, time
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ..models import dbFunctions as functions
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
        #data = {'update':'OK'}
        #functions.createObject(RepairBooking, CONST_Rep)
        #for each in request.POST.get('confirmList').split(','):
        #    booking = RepairBooking.objects.get(id=each)
        #    booking.confirm = True
        #    booking.save()
        return JsonResponse({'update': functions.updateObject("His", {"confm": True})})


def __getBooking(confirmStatus=None):
    if confirmStatus is not None:
        return render_to_response('table_0.html', {'result': functions.getAllObjects("Rep", {"confm": confirmStatus})})
    return render_to_response('table_0.html', {'result': functions.getAllObjects("Rep")})


@login_required(login_url='dangnhap')
def showBooking_all(request):
    return __getBooking()


@login_required(login_url='dangnhap')
def showBooking_notConfirm(request):
    return __getBooking(False)


@login_required(login_url='dangnhap')
def showBooking_confirmed(request):
    return __getBooking(True)


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
    history = functions.getAllObjects("His")
    webParam[WEB_DATA] = {'danhsachXe': history, 'number': len(history)}
    return pageReturn(request, DICH_VU)


@login_required(login_url='dangnhap')
def themxevaotram(request):
    if request.method == 'POST':
        history_id = functions.createObject_FrRequest("His", request, request.POST.get('pho')).id
        functions.updateObject("His", history_id, {'din':datetime.datetime.fromtimestamp(int(time.time())).strftime("%d-%m-%Y - %H:%M")})
        return render_to_response('themxedangsuachua.html', {'danhsachXe': functions.getObject("His", {"id": history_id}, isDictReturn=True)})


@login_required(login_url='dangnhap')
def thanhtoantienDichvu(request):
    if request.method == 'POST':
        result = {'result': 'OK'}
        return JsonResponse(result)


@login_required(login_url='dangnhap')
def getPhoneBookingList(request):
    if request.method == 'POST':
        today = time.time().strftime("%d-%m-%Y")
        bookingDict = functions.getAllObjects("Rep", {"confm": True, "datep": today})
        #print("No: ", len(bookingDict), "Bookings: ", bookingDict.keys())
        listPhoneBooking = []
        data = {}
        for eachBookingID in bookingDict.keys():
            oneBooking = bookingDict[eachBookingID]
            print("One-Booking: ", oneBooking)
            listPhoneBooking.append(oneBooking['phone'][1])
            subData = {}
            for each in CONST_His.keys():
                if each in oneBooking.keys():
                    subData[each] = oneBooking[each][1]
                else:
                    subData[each] = ""
            subData['cus'] = oneBooking['cname'][1]
            subData['din'] = time.time().strftime("%d-%m-%y lúc %H:%M")
            subData['amt'] = "0"
            subData['mec'] = ""
            data[eachBookingID] = subData
        #print(listPhoneBooking)
        #print(data)
        return JsonResponse({'listPhoneBooking':listPhoneBooking, 'bookingDetail': data})
