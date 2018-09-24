import datetime, time, json
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import Member
from ..models import RepairBooking
from ..Folder_pyFile.baseMenu import DICH_VU, NHAN_VIEN, webParam, WEB_DATA
from ..Folder_pyFile.navMenu import pageReturn
from ..Folder_pyFile import jsonFile


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
        dataHistory = jsonFile.readFile(pathFile = HISTORY_FOLDER, fileName = request.POST.get('usr'))
        if dataHistory is not None:
            data = {'summary': dataHistory['summary'],
                    'history': getHistory(dataHistory['earning']),
                    'using': getHistory(dataHistory['spending'])}
        return JsonResponse(data)

def getDict(data=None, isKeys=True):
    items = {'cus':'Tên khách',
             'pho':'Điện thoại',
             'mod':'Loại xe',
             'mil':'Số km',
             'ser':'Dịch vụ',
             'mec':'Tên thợ',
             'amt':'Thành tiền',
             'din' :'Ngày giờ'
            }
    if isKeys and data is None:
        return list(items.keys())
    else:
        result = {}
        for each in data:
            result[each] = {}
            for key in data[each]:
                result[each][key] = {'val':data[each][key], 'str':items[key]}
        return result, len(result)


@login_required(login_url='dangnhap')
def danhsachxedangsuachua(request):
    data, size = getDict(data=jsonFile.danhsachxedangsuachua(),isKeys=False)
    webParam[WEB_DATA] = {'danhsachXe': data, 'number': size}
    return pageReturn(request, DICH_VU)


@login_required(login_url='dangnhap')
def themxevaotram(request):
    if request.method == 'POST':
        id = str(int(time.time()))
        data = {id: {}}
        for each in getDict():
            data[id][each] = request.POST.get(each)
        data[id]['din'] = datetime.datetime.utcfromtimestamp(int(id)).strftime("%d-%m-%y lúc %H:%M")
        jsonFile.themxevaotram(data = data)
        result, size = getDict(data=data,isKeys=False)
        return render_to_response('themxedangsuachua.html', {'danhsachXe': result})

def cusData(data):
    result = {}
    for each in data.keys():
        if each != 'timestamp' and each != 'pho':
            result[each] = data[each]
    return {data['timestamp']: result}

def getDataFrRequest(request):
    #timestamp = request.POST.get('timestamp')
    temp = {"timestamp": request.POST.get('timestamp')}
    for each in getDict():
        key = 'serviceData[' + each + ']'
        temp[each] = request.POST.get(key)
    return temp['pho'], cusData(temp), request.POST.get('timestamp')

@login_required(login_url='dangnhap')
def thanhtoantienDichvu(request):
    if request.method == 'POST':
        result = {'result': 'OK'}
        #postData = getDataFrRequest(request)
        fileName, dictData, timestamp_id= getDataFrRequest(request)
        jsonFile.themDichvu(fileName=fileName, data=dictData, timestamp_id=timestamp_id)
        return JsonResponse(result)


@login_required(login_url='dangnhap')
def getPhoneBookingList(request):
    if request.method == 'POST':
        listPhoneBooking = []
        today = datetime.datetime.utcfromtimestamp(time.time()).strftime("%d-%m-%Y")
        bookings = RepairBooking.objects.all().filter(confirm=True, date=today)
        #bookings = RepairBooking.objects.all().filter(date=today)
        data = {}
        id = str(int(time.time()))
        for eachIterator in list(bookings.values()):
            #print(eachIterator)
            listPhoneBooking.append(eachIterator['phone'])
            #print(eachIterator.keys())
            data[id] = {}
            for each in eachIterator.keys():
                #print(each[:3])
                if each[:3] in getDict():
                    data[id][each[:3]] = eachIterator[each]
            data[id]['cus'] = eachIterator['name']
            data[id]['din'] = datetime.datetime.utcfromtimestamp(int(id)).strftime("%d-%m-%y lúc %H:%M")
            data[id]['amt'] = "0"
            data[id]['mec'] = ""
            id = str(int(id) + 1)
        #print(listPhoneBooking)
        #print(data)
        return JsonResponse({'listPhoneBooking':listPhoneBooking, 'bookingDetail': data})
