from .baseMenu import LEFT, THANH_VIEN
#from .models import ProductCaterogy as Category

def getMenu(menuData):
    #print(menuData[LEFT][THANH_VIEN[0]])
    #print(menuData[LEFT][THANH_VIEN[0]]['subMenu'])
    menuData[LEFT][THANH_VIEN[0]]['subMenu'] = { 'thongtincanhan'  : 'Thông tin cá nhân',
                                                  'thongtinxe'      : 'Thông tin xe',
                                                  'dangxuat'        : 'Đăng xuất',
                                                }
    return menuData
