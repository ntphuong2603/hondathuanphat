import json
from pathlib import Path


HISTORY_FOLDER = 'webhondathuanphat\\Folder_json\\history\\'
FILE_DSXDSC = 'xeDangSuaChua'


def fileExists(pathFile, fileName):
    return Path(pathFile + fileName + ".json").exists()


def openJsonFile(pathFile, fileName):
    return open(pathFile + fileName + '.json', 'r', encoding='utf-8')


def createJsonFile(pathFile, fileName):
    return open(pathFile + fileName + '.json', 'w+', encoding='utf-8')


def getJsonFile(pathFile, fileName):
    return open(pathFile + fileName + '.json', 'w', encoding='utf-8')


def getData(pathFile, fileName):
    if fileExists(pathFile, fileName):
        fileOpen = openJsonFile(pathFile, fileName)
        fileData = fileOpen.read()
        if len(fileData) == 0:
            dictData = {}
        else:
            dictData = json.loads(fileData)
        fileOpen.close()
        return dictData
    else:
        return {}


def createFile(pathFile, fileName):
    if fileExists(pathFile, fileName):
        return False, None
    else:
        return True, createJsonFile(pathFile, fileName)


def dict2Json(dictData):
    return json.dumps(dictData, indent = 3, ensure_ascii = False)


def writeJson(pathFile, fileName, dictData, isAppend=False):
    if isAppend:
        data = getData(pathFile, fileName)
        print('jsonFile.py: ', data)
        for each in dictData:
            data[each] = dictData[each]
        print('jsonFile.py: ', data)
    else:
        data = dictData
    file = getJsonFile(pathFile, fileName)
    file.write(dict2Json(data))
    file.close()
    return True


def danhsachxedangsuachua():
    return getData(pathFile = HISTORY_FOLDER, fileName = FILE_DSXDSC)


def themxevaotram(data):
    if not fileExists(pathFile = HISTORY_FOLDER, fileName = FILE_DSXDSC):
        createFile(pathFile = HISTORY_FOLDER, fileName = FILE_DSXDSC)
    return writeJson(pathFile = HISTORY_FOLDER, fileName = FILE_DSXDSC, dictData = data, isAppend = True)



def themDichvu(fileName, data, timestamp_id):
    if not fileExists(pathFile = HISTORY_FOLDER, fileName = fileName):
        createFile(pathFile = HISTORY_FOLDER, fileName = fileName)
    numberXeDangSuaChua = danhsachxedangsuachua()
    del numberXeDangSuaChua[timestamp_id]
    writeJson(pathFile = HISTORY_FOLDER, fileName = FILE_DSXDSC, dictData = numberXeDangSuaChua)
    return writeJson(pathFile = HISTORY_FOLDER, fileName = fileName, dictData = data, isAppend = True)
