from django.shortcuts import render
from .baseMenu import TRANG_CHU, BAN_HANG, DICH_VU, PHU_TUNG, LAI_XE_AN_TOAN, THANH_VIEN, TIN_TUC, TUYEN_DUNG
from .baseMenu import webParam, get_HTML_File, LOAI_XE, LEFT, RIGHT, WEB_PARAM
from ..models import ProductCaterogy as Caterogy

#Constant menu variables
MENU_POSITION = 6

mainMenuList = [TRANG_CHU, BAN_HANG, DICH_VU, PHU_TUNG, LAI_XE_AN_TOAN, THANH_VIEN, TIN_TUC, TUYEN_DUNG]

subMenuList = { DICH_VU[0]     : { 'henlichsuachua'    : 'Hẹn lịch sửa chữa',
                              },
                THANH_VIEN[0]  : { 'dangky'        : 'Đăng ký',
                                   'dangnhap'      : 'Đăng nhập',
                                 },
              }

menuList = {LEFT: None, RIGHT: None}


def createSubMenu_BANHANG():
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


def createMenuList(isLeftMenu):
    listMenu = mainMenuList[1:MENU_POSITION]
    menuList[isLeftMenu] = {}
    if isLeftMenu==RIGHT:
        listMenu = mainMenuList[MENU_POSITION:len(mainMenuList)]
    for each in range(len(listMenu)):
        menuDict = {}
        menuCode = listMenu[each][0]
        menuName = listMenu[each][1]
        subMenu = None
        if menuCode in subMenuList.keys():
            subMenu = subMenuList[menuCode]
        menuDict['menuName'] = menuName
        menuDict['subMenu'] = subMenu
        menuList[isLeftMenu][menuCode] = menuDict


def getMenuList(isLeftMenu):
    #print(menuList)
    if menuList[isLeftMenu] is None:
        createMenuList(isLeftMenu);
    #print(menuList)
    return menuList[isLeftMenu]


def getMenu():
    createSubMenu_BANHANG()
    return {LEFT : getMenuList(LEFT),
            RIGHT : getMenuList(RIGHT),
            WEB_PARAM: webParam,
            }
