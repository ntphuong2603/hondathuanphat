from django.shortcuts import render
from .baseMenu import BAN_HANG, DICH_VU,THANH_VIEN, LOAI_XE, WEB_PARAM, LEFT, RIGHT, MENU_NAME, SUB_MENU
from .baseMenu import webParam, getSubMenuList
from ..models import ProductCaterogy as Caterogy
from .baseMenu import loadData

#Constant menu variables
subMenuList = { DICH_VU[0]     : { 'henlichsuachua'    : 'Hẹn lịch sửa chữa',
                                 },
                THANH_VIEN[0]  : { 'dangky'        : 'Đăng ký',
                                   'dangnhap'      : 'Đăng nhập',
                                 },
              }


def createSubMenu_BANHANG():
    if not BAN_HANG[0] in subMenuList.keys():
        subMenu = {}
        data = loadData()
        for each in data.keys():
            subMenu[each] = data[each]['name']
            if webParam[LOAI_XE] is None:
                webParam[LOAI_XE] = str(each)
            else:
                webParam[LOAI_XE] = webParam[LOAI_XE] + str(each)
        subMenuList[BAN_HANG[0]] = subMenu
    #print(subMenuList)


def createSubMenu_BANHANG_OLD():
    if not BAN_HANG[0] in subMenuList.keys():
        subMenu = {}
        caterogyList = Caterogy.objects.all()
        for each in caterogyList:
            subMenu[str(each.id)] = each.name
            if webParam[LOAI_XE] is None:
                webParam[LOAI_XE] = str(each.id)
            else:
                webParam[LOAI_XE] = webParam[LOAI_XE] + str(each.id)
        subMenuList[BAN_HANG[0]] = subMenu
    #print(subMenuList)


def getMenu(menuData):
    createSubMenu_BANHANG()
    #print('KHACH - BEFORE: ', menuData)
    menuData = getSubMenuList(menuList=menuData, subMenuList=subMenuList)
    #print('KHACH - AFTER: ', menuData)
    return {LEFT : menuData[LEFT],
            RIGHT : menuData[RIGHT],
            WEB_PARAM: webParam,
           }
