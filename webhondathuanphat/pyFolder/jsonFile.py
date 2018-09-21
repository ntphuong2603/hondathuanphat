import json
from pathlib import Path

def readFile(pathFile=None, fileName=None):
    jsonData = None
    try:
        fileOpen = open(pathFile + fileName + '.json', 'r', encoding='utf-8')
        jsonData = json.loads(fileOpen.read())
        fileOpen.close()
    except Exception as e:
        print(e)
    return jsonData

def createFile(pathFile=None, fileName=None):
    try:
        file = Path(pathFile + fileName + ".json")
        if file.exists():
            return False
        else :
            fileOpen = open(file, 'w', encoding = 'utf-8')
            fileOpen.close()
            return True
    except Exception as e:
        print(e)

def writeJson(pathFile, fileName, dict_data):
    try:
        if dict_data.instantOf(dict):
            json_data = json.dumps(dict_data, indent=3, ensure_ascii=False)
            f = open(fileName, 'w', encoding = 'utf-8')
            f.write(json_data)
            f.close()
    except Exception as e:
        print(e)

def appendJson(pathFile, fileName, dict_data):
    try:
        if dict_data.instantOf(dict):
            json_data = json.dumps(dict_data, indent=3, ensure_ascii=False)
            f = open(fileName, 'w+', encoding = 'utf-8')
            f.write(json_data)
            f.close()
    except Exception as e:
        print(e)
