import datetime
from django.http import JsonResponse
from django.contrib.auth.models import User
from ..Folder_pyFile.baseMenu import DICH_VU, webParam, WEB_DATA
from ..Folder_pyFile.navMenu import pageReturn
from ..models import dbFunctions as functions
from ..models.RepairBooking import RepairBooking, CONST
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
        data = {}
        try:
            print('Data: ', request.POST)
            print('File: ', request.FILES)
            data = functions.getDataFrRequest(request.POST, CONST)
            user = functions.getUser(data['phone'])
            book = functions.createObject(RepairBooking, data)
            data['result'] = 'OK'
        except Exception as e:
            print("Error: ", e)
            data['result'] = 'NG'
        return JsonResponse(data)
    else:
        webParam['webData'], webParam['modelList'] = getData()
        return pageReturn(request, DICH_VU)
