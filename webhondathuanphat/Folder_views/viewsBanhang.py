from ..Folder_pyFile.baseMenu import BAN_HANG, webParam, WEB_DATA
from ..Folder_pyFile.baseMenu import loadData
from ..Folder_pyFile.navMenu import pageReturn
import json


CAT = 'caterogy'
MOD = 'model'
DATA = {CAT: None, MOD: None}
COLOR = 'colorName'
PRICE = 'price'
PICTURE = 'picture'

def loadData_OLD(is_Model=False):
    fileName = FILE_CATEROGY
    if is_Model:
        fileName = FILE_MODEL
    f = open(fileName, 'r', encoding = 'utf-8')
    dict_data = json.loads(f.read())
    f.close()
    return dict_data

def getModelList():
    modelList = []
    modelData = getData()
    for eachKey in modelData.keys():
        modelList.append(modelData[eachKey]['spec']['Tên sản phẩm'])
    return sorted(modelList)

def getData():
    if DATA[MOD] is None:
        DATA[MOD] = loadData(is_Model=True)
    return DATA[MOD]

def getCaterogy():
    if DATA[CAT] is None:
        DATA[CAT] = loadData(is_Model=False)
    return DATA[CAT]


def loadModel(modelList):
    result = {}
    #print(dict_model)
    for each in modelList:
        singleOne = list(getData()[each]['data'].items())[0][1]
        #print(singleOne)
        result[each] = {
                        'name': each.upper()[:10],
                        'color': singleOne[COLOR],
                        PRICE: "Liên hệ để biết giá",
                        PICTURE:singleOne[PICTURE]
                       }
    #print(json.dumps(result, indent=3))
    return result


def theoLoaixe(request, loaiXe:int):
    #print(str(request)[-1])
    strRequest = str(request).strip()
    cat = strRequest[strRequest.rfind('/')+1:]
    cat = cat.replace('>','').replace("'",'')
    cat_dict = getCaterogy()
    result = None
    webParam[WEB_DATA] = loadModel(cat_dict[cat]['list'])
    return pageReturn(request, BAN_HANG)


def loadModel_Full(modelName):
    result = getData()[modelName]
    result['number'] = range(len(result['data']))
    result['active'] = list(result['data'].items())[0][0]
    #print(json.dumps(result, indent=4))
    return result


def theoDoixe(request, doiXe:str):
    webParam[WEB_DATA] = loadModel_Full(doiXe)
    #webParam[WEB_DATA] = getData()[doiXe]
    return pageReturn(request, BAN_HANG)
