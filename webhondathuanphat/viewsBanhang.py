from .pyFolder.baseMenu import BAN_HANG, webParam, WEB_DATA
from .pyFolder.navMenu import pageReturn
import json

JSON_FOLDER = 'webhondathuanphat\\jsonFolder\\'
FILE_CATEROGY = JSON_FOLDER + 'dict_cat.json'
FILE_MODEL = JSON_FOLDER + 'dict_Model.json'
DATA = {'cate': None, 'model': None}
NAME = 'name'
COLOR = 'color-name'
PRICE = 'price'
PICTURE = 'picture'

def loadData(is_Model=False):
    fileName = FILE_CATEROGY
    if is_Model:
        fileName = FILE_MODEL
    f = open(fileName, 'r', encoding = 'utf-8')
    dict_data = json.loads(f.read())
    f.close()
    return dict_data


def getData():
    if DATA['model'] is None:
        DATA['model'] = loadData(is_Model=True)
    return DATA['model']


def getCaterogy():
    if DATA['cate'] is None:
        DATA['cate'] = loadData(is_Model=False)
    return DATA['cate']


def loadModel(modelList):
    result = {}
    #print(dict_model)
    for each in modelList:
        singleOne = list(getData()[each]['data'].items())[0][1]
        #print(singleOne)
        result[each] = {
                        NAME: each.upper(),
                        'color': singleOne[COLOR],
                        PRICE: singleOne[PRICE],
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
    #print('Caterogy: ', cat)
    if cat == '1':
        models = []
        for eachKey in cat_dict.keys():
            for eachModel in cat_dict[eachKey]:
                models.append(eachModel)
        result = models
    else:
        result = cat_dict[cat]
    #print(result)
    webParam[WEB_DATA] = loadModel(result)
    return pageReturn(request, BAN_HANG)


def loadModel_Full(modelName):
    result = {}
    dataModel = getData()[modelName]
    for eachKey in dataModel.keys():
        if eachKey is dict:
            for each in eachKey.keys():
                result[each] = eachKey[each]
        else:
            result[eachKey] = dataModel[eachKey]
    #print(result)
    return result


def theoDoixe(request, doiXe:str):
    webParam[WEB_DATA] = loadModel_Full(doiXe)
    return pageReturn(request, BAN_HANG)
