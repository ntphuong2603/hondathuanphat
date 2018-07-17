from django.shortcuts import render
from .baseMenu import webParam, SELECTED_MENU, get_HTML_File, LEFT, RIGHT, WEB_PARAM
from .navMenuKhach import getMenu as menu_Khach
from .navMenuNhanvien import getMenu as menu_Nhanvien
from .navMenuThanhvien import getMenu as menu_Thanhvien


def pageReturn(request, webPage):
    webParam[SELECTED_MENU] = webPage[0]
    print(get_HTML_File(request=request))
    html_file = get_HTML_File(request=request)
    menuData = menu_Khach()
    #print(menuData)
    if request.user.is_authenticated:
        if request.user.is_staff:
            menuData = menu_Nhanvien()
        else:
            menuData = menu_Thanhvien(menuData)
    #print(menuData[WEB_PARAM])
    try:
        return render(request, html_file,
                        {'leftMenu' : menuData[LEFT],
                         'rightMenu': menuData[RIGHT],
                         'webParam' : menuData[WEB_PARAM],
                         }
                      )
    except Exception as e:
        #print(e)
        return render(request, 'error.html')
