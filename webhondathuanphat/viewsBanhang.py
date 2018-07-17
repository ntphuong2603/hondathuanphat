from .pyFolder.baseMenu import BAN_HANG, webParam, WEB_DATA
from .pyFolder.navMenu import pageReturn


def theoLoaiXe(request, loaiXe:int):
    if loaiXe > 1:
        webParam[WEB_DATA] = range(5)
    else:
        webParam[WEB_DATA] = range(10)
    return pageReturn(request, BAN_HANG)
