from django.contrib.auth.models import User as Usr
from .Member import Member as Mbr, CONST as CONST_Mbr
from ..models.RepairBooking import RepairBooking as Rep, CONST as CONST_Rep
from ..models.History import History as His, CONST as CONST_His

__CONST_Usr = {
    "username":"Tên đăng nhập",
    "first_name":"Tên",
    "last_name":"Họ",
    "email":"Địa chỉ email",
    #"password":"Mật khẩu",
    #{}"is_superuser":"Quản trị chính",
    #{}"is_staff":"Nhân viên",
    #{}"is_active":"Tình trạng",
    "date_joined":"Ngày đăng ký"
}

__CONST = {
    "Usr" : {"cls": Usr, "cst": __CONST_Usr},
    "Mem" : {"cls": Mbr, "cst": CONST_Mbr},
    "Rep" : {"cls": Rep, "cst": CONST_Rep},
    "His" : {"cls": His, "cst": CONST_His}
}


def __query_ToDict(className, queryValues):
    #print("Query values: ", queryValues)
    classConstant = __CONST[className]["cst"]
    dictData = {}
    for key in classConstant.keys():
        if key in queryValues.keys():
            dictData[key] = [classConstant[key], queryValues[key]]
    #print(dictData)
    return {queryValues["id"]:dictData}


def __querySet_ToDict(className, querySet):
    result = {}
    #print("QuerySet: ", querySet)
    if len(querySet) == 1:
        #print("SIZE 1")
        result.update(__query_ToDict(className, querySet.values()[0]))
    else:
        #print("Size OVER 1", querySet.values())
        #querySet is query.values()
        for eachQuery in querySet.values().iterator():
            #print(eachQuery)
            result.update(__query_ToDict(className, eachQuery))
    return result


#request must be in "FormData" type
def __getDataFrRequest(className, request):
    dataReturn = {}
    classConstant = __CONST[className]["cst"]
    for each in classConstant.keys():
        value = request.POST.get(each)
        if not value is None:
            dataReturn[each] = value
    return dataReturn


def createObject(className, objDict=None):
    print("data of object: ", objDict)
    try:
        if objDict is not None:
            obj = __CONST[className]["cls"](**objDict)
        else:
            obj = __CONST[className]["cls"]()
        obj.save()
        return obj
    except Exception as e:
        print("Error [createObject]: ",e)
        return None


def createObject_FrRequest(className, request, username=None):
    dataDict = __getDataFrRequest(className, request)
    if username is not None:
        #user = getUser(username)
        #print(user, list(user.keys())[0])
        dataDict.update({"usr_id": list(getUser(username).keys())[0]})
    return createObject(className, dataDict)


def getObject(className, objCond, isDictReturn=True):
    objs = __CONST[className]['cls'].objects.all().filter(**objCond)
    if isDictReturn:
        return __querySet_ToDict(className, objs)
    return objs


def updateObject(className, obj_id, dataDict):
    try:
        obj = __CONST[className]['cls'].objects.filter(pk=obj_id)
        obj.update(**dataDict)
        return True
    except Exception as e:
        print("Error [updateObject]:", e)
        return False


def deleteObject(className, obj_id):
    try:
        updateObject(className, obj_id, {"isD":True})
    except Exception as e:
        print("Error [deleteObject]:", e)
        return False


#create new user if username does NOT exist
def get_create_User(username, isCreate=False, password=None):
    clsUsr = __CONST["Usr"]["cls"]
    user = clsUsr.objects.all().filter(username=username)
    if not user.exists() and isCreate:
        user = clsUsr(username=username, email='')
        user.set_password(username)
        if password is not None:
            user.set_password(password)
        user.save()
        member = createObject("Mem", {"usr": user})
    return user


def getUser(username, isDictReturn=True):
    if isDictReturn:
        return __querySet_ToDict("Usr", get_create_User(username, False, None))
    return get_create_User(username, False, None)


def createUser(username, password=None):
    return get_create_User(username, True, password)


def getAllObjects(className, condDict=None, isDictReturn=True):
    if condDict is None:
        condDict = {"isD":False}
    else:
        condDict.update({"isD":False})
    querySet = __CONST[className]["cls"].objects.all().filter(**condDict)
    if isDictReturn:
        return __querySet_ToDict(className, querySet)
    else:
        return querySet


def getAll_Deleted(className, condDict=None):
    if condDict is None:
        condDict = {"isD": True}
    else:
        condDict.update({"isD": True})
    return getAllObjects(className, condDict)
