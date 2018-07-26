from django.shortcuts import render
from .baseMenu import MOBILE
from .baseMenu import TRANG_CHU, BAN_HANG, DICH_VU, PHU_TUNG, LAI_XE_AN_TOAN, THANH_VIEN, TIN_TUC, TUYEN_DUNG, NHAN_VIEN
from .baseMenu import webParam, SELECTED_MENU, get_HTML_File, LEFT, RIGHT, WEB_PARAM, ERROR_HTML_FILE, MENU_NAME, SUB_MENU
from .navMenuKhach import getMenu as menu_Khach
from .navMenuNhanvien import getMenu as menu_Nhanvien
from .navMenuThanhvien import getMenu as menu_Thanhvien

MENU_POSITION = 6

mainMenuList = [TRANG_CHU, BAN_HANG, DICH_VU, PHU_TUNG, LAI_XE_AN_TOAN, THANH_VIEN, TIN_TUC, TUYEN_DUNG]

MOBILES = ['iphone', 'ipad', 'android']

def initial_Menu(menuData):
    for eachSide in [LEFT, RIGHT]:
        if menuData[eachSide] is None:
            menuData[eachSide] = {}
            if eachSide == LEFT:
                listMenu = mainMenuList[1: MENU_POSITION]
            else:
                listMenu = mainMenuList[MENU_POSITION:len(mainMenuList)]
            for each in listMenu:
                menuCode = each[0]
                menuName = each[1]
                menuData[eachSide][menuCode] = {MENU_NAME: menuName, SUB_MENU: None}
    return menuData


def isMobile(strDevices):
    #ua = request.META.get('HTTP_USER_AGENT', '').lower()
    for eachMobile in MOBILES:
        if strDevices.find(eachMobile) > 0:
            return MOBILE
    return None


def pageReturn(request, webPage):
    #initial_Menu()
    menuData = menu_Khach(initial_Menu(menuData = {LEFT: None, RIGHT: None}))
    #print()
    #print('MENU - BEFORE: ')
    #print(menuData)
    #print()
    if request.user.is_authenticated:
        if request.user.is_staff:
            del menuData[LEFT][THANH_VIEN[0]]
            menuData[LEFT][NHAN_VIEN[0]] = {MENU_NAME: NHAN_VIEN[1], SUB_MENU: None}
            menuData = menu_Nhanvien(menuData)
        else:
            menuData = menu_Thanhvien(menuData)
    #print()
    #print('MENU - AFTER: ')
    #print(menuData)
    #print()
    webParam[SELECTED_MENU] = webPage[0]
    #print(get_HTML_File(request=request))
    html_file = get_HTML_File(request=request)
    print("File html template: ", html_file)
    print(request.META['HTTP_USER_AGENT'])
    print(request.META['REMOTE_ADDR'])
    #print(request.keys())
    webParam[MOBILE] = isMobile(request.META.get('HTTP_USER_AGENT', '').lower())
    try:
        return render(request, html_file,
                        {'leftMenu' : menuData[LEFT],
                         'rightMenu': menuData[RIGHT],
                         'webParam' : menuData[WEB_PARAM],
                         }
                      )
    except Exception as e:
        print(e)
        return render(request, ERROR_HTML_FILE)
