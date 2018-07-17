from .baseMenu import LEFT, THANH_VIEN
#from .models import ProductCaterogy as Category

def getMenu(menuData):
    menuData[LEFT][THANH_VIEN[0]] = { 'thongtincanhan'  : 'Thông tin cá nhân',
                                      'thongtinxe'      : 'Thông tin xe',
                                      'dangxuat'        : 'Đăng xuất',
                                    }
    return menuData
