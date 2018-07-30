#Constant menu variables
TRANG_CHU       = ('trangchu',      'Trang chủ')
BAN_HANG        = ('banhang',       'Bán hàng')
DICH_VU         = ('dichvu',        'Dịch vụ')
PHU_TUNG        = ('phutung',       'Phụ tùng')
LAI_XE_AN_TOAN  = ('laixeantoan',   'Lái xe an toàn')
THANH_VIEN      = ('thanhvien',     'Thành viên')
TIN_TUC         = ('tintuc',        'Tin tức')
TUYEN_DUNG      = ('tuyendung',     'Tuyển dụng')
TRANH_DANG_NHAP = ('trangDangnhap', 'Trang đăng nhập')
NHAN_VIEN       = ('nhanvien',      'Nhân viên')

SELECTED_MENU = 'selectedMenu'
JS_FILE = 'jsFile'
WEB_DATA = 'webData'
WEB_PARAM = 'webParam'
LOAI_XE = 'loaiXe'
MOBILE = 'mobile'
LEFT = 'left'
RIGHT = 'right'
MENU_NAME = 'menuName'
SUB_MENU = 'subMenu'
ERROR_HTML_FILE = 'error.html'

webParam = {SELECTED_MENU: None, JS_FILE: None, WEB_DATA: None, LOAI_XE: None, MOBILE: None}

def get_HTML_File(request):
    requestPathString = request.path.replace('/', '').strip()
    if len(requestPathString) == 0:
        requestPathString = TRANG_CHU[0]
    webParam['jsFile'] = 'js/' + requestPathString + '.js'
    if (requestPathString.find('theoLoaixe') > 1) :
        requestPathString = 'banhangtheoLoaixe'
    elif (requestPathString.find('theoDoixe') > 1) :
        requestPathString = 'banhangtheoDoixe'
    return (requestPathString + '.html')


def getSubMenuList(menuList, subMenuList):
    #print(menuList.keys())
    for eachSide in [LEFT, RIGHT]:
        for eachMenu in menuList[eachSide].keys():
            #print(subMenuList.keys())
            if eachMenu in subMenuList.keys():
                #print(menuList[eachMenu][SUB_MENU])
                #print(menuList[eachSide][eachMenu][SUB_MENU])
                #print(subMenuList[eachMenu])
                menuList[eachSide][eachMenu][SUB_MENU] = subMenuList[eachMenu]
    return menuList
