from django.http import JsonResponse
import datetime
from ..Folder_pyFile.baseMenu import DICH_VU, webParam, WEB_DATA
from ..Folder_pyFile.navMenu import pageReturn
from ..models import RepairBooking
from ..Folder_views.viewsBanhang import getModelList as modelList

#Service view funtions
def getData():
    today = datetime.date.today().strftime("%d-%m-%Y")
    #print(today)
    todaylist = []
    for i in range(10):
        today = datetime.date.today() + datetime.timedelta(days=i)
        todaylist.append(today.strftime("%d-%m-%Y"))
    return todaylist, modelList


def henlichsuachua(request):
    if request.method == 'POST':
        data = {'result' : 'OK'}
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            model = request.POST.get('model')
            date = request.POST.get('date')
            time = request.POST.get('time')
            symptom = request.POST.get('symptom')
            partList = request.POST.get('partList')
            rb = RepairBooking(name=name, phone=phone, model=model, date=date, time=time, symptom=symptom, partList=partList)
            rb.save()
        except Exception as e:
            data['result'] = 'NG'
        return JsonResponse(data)
    else:
        webParam['webData'], webParam['modelList'] = getData()
        return pageReturn(request, DICH_VU)
