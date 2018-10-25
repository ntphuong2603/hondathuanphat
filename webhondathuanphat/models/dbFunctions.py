from django.contrib.auth.models import User
from .Member import Member

def makeDict(querySet, result, className):
    for eachIterator in querySet.iterator():
        for eachKey in eachIterator.keys():
            if eachKey in className.keys():
                strList = [className[eachKey], eachIterator[eachKey]]
                result[eachKey] = strList
    #print(result)
    return result

def queryTOdict(querySet, CONST):
    result = {}
    for each in querySet.iterator():
        #print(each)
        val = {}
        for key in CONST.keys():
            if key in each.keys():
                val[key] = [CONST[key], each[key]]
        result[each["id"]] = val
    return result

def getUser(username, password=None):
    if not User.objects.filter(username=username).exists():
        user = User(username=username, email='')
        if password is None:
            user.set_password(username)
        else:
            user.set_password(password)
        user.save()
        member = Member(user=user)
        member.save()
    else:
        user = User.objects.get(username=username)
    return user

def getDataFrRequest(requestDict, stdDict):
    result = {}
    print(stdDict)
    for each in requestDict.keys():
        result[each] = requestDict[each]
    print(result)
    return result

def createObject(cls, dic, username=None):
    obj = cls()
    if not username is None:
        obj = cls(usr=getUser(username))
    obj.save()
    for key in dic.keys():
        if not dic[key] is None:
            setattr(obj, key, dic[key])
    #print(obj, dic.values())
    obj.save()
    return obj

def getObject(cls, obj_id):
    obj = cls.objects.filter(id=obj_id, isD=False)
    if obj.exists():
        return obj
    return None

def updateObject(cls, obj_id, dic):
    obj = getObject(cls, obj_id)
    if not obj is None:
        for key in dic.keys():
            if not dic[key] is None:
                setattr(obj.values(), key, dic[key])
        return True
    return False

def deleteObject(cls, obj_id):
    obj = getObject(cls, obj_id)
    if not obj is None:
        setattr(obj, isD, True)
        obj.save()
        return True
    return False

def getAll(cls, CONST, conditionDict=None):
    #objList = cls.objects.all().filter(isD=False).values()
    #print(objList)
    result = queryTOdict(cls.objects.all().filter(isD=False).values(), CONST)
    #print(len(result))
    resultReturn = {}
    if not (conditionDict is None or result is None):
        for eachID in result.keys():
            oneElement = result[eachID]
            ok_flag = True
            for eachKey in conditionDict.keys():
                #print(result[eachElement], eachKey, conditionDict[eachKey])
                if not oneElement[eachKey][1] == conditionDict[eachKey]:
                    ok_flag = False
                    break
            if ok_flag:
                #print(eachID, oneBooking)
                resultReturn[eachID] = oneElement
        #print(len(resultReturn))
        return resultReturn
    return result
