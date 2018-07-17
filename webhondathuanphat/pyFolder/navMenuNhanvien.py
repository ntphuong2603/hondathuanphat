from django.shortcuts import render
from .baseMenu import DICH_VU, NHAN_VIEN
from .baseMenu import webParam, get_HTML_File

mainMenuList = [DICH_VU, NHAN_VIEN]

subMenuList = { DICH_VU[0]  : { 'xemlichhensuachua' : 'Xem lịch hẹn sửa chữa',
                              },
                NHAN_VIEN[0]: { 'thongtincanhan'    : 'Thông tin cá nhân',
                                'dangxuat'          : 'Đăng xuất',
                              },
              }

def loadMenu():
    returnMenu = {}
    for each in range(len(mainMenuList)):
        menuDict = {}
        menuCode = mainMenuList[each][0]
        menuName = mainMenuList[each][1]
        subMenu = subMenuList[menuCode]
        menuDict['menuName'] = menuName
        menuDict['subMenu'] = subMenu
        #print(menuDict)
        returnMenu[menuCode] = menuDict
    #print(returnMenu)
    return returnMenu


def getMenu():
    return {LEFT : loadMenu(),
            RIGHT : None,
            WEB_PARAM: webParam,
            }
    
