from .baseMenu import THANH_VIEN, LEFT, RIGHT, WEB_PARAM
from .baseMenu import webParam, getSubMenuList

subMenuList = { THANH_VIEN[0]  : { 'thongtinthanhvien'  : 'Thông tin cá nhân',
                                   'thongtinxe'      : 'Thông tin xe',
                                   'dangxuat'        : 'Đăng xuất',
                                 }
              }


def getMenu(menuData):
    #print('THANH VIEN - BEFORE', menuData)
    menuList = getSubMenuList(menuList=menuData, subMenuList=subMenuList)
    #print('THANH VIEN - AFTER', menuData)
    return {LEFT : menuList[LEFT],
            RIGHT : menuList[RIGHT],
            WEB_PARAM: webParam,
           }
