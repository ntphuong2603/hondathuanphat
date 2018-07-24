from django.shortcuts import render
from .baseMenu import LEFT, RIGHT, WEB_PARAM, BAN_HANG, DICH_VU, NHAN_VIEN
from .baseMenu import webParam, get_HTML_File, getSubMenuList

mainMenuList = [DICH_VU, NHAN_VIEN]

subMenuList = { BAN_HANG[0] : { 'loaixe': 'Loại xe',
                              },
                DICH_VU[0]  : { 'xemlichhensuachua' : 'Xem lịch hẹn sửa chữa',
                              },
                NHAN_VIEN[0]: { 'thongtinnhanvien'    : 'Thông tin cá nhân',
                                'dangxuat'          : 'Đăng xuất',
                              },
              }


def getMenu(menuData):
    #print('KHACH - BEFORE: ', menuData)
    menuData = getSubMenuList(menuList=menuData, subMenuList=subMenuList)
    #print('KHACH - AFTER: ', menuData)
    return {LEFT : menuData[LEFT],
            RIGHT : menuData[RIGHT],
            WEB_PARAM: webParam,
           }
