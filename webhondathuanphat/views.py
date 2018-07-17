from .pyFolder.baseMenu import TRANG_CHU, BAN_HANG, DICH_VU, PHU_TUNG, LAI_XE_AN_TOAN, THANH_VIEN, TIN_TUC, TUYEN_DUNG
from .pyFolder.navMenu import pageReturn


# Create your views here.
def trangchu(request):
    return pageReturn(request, TRANG_CHU)


def banhang(request):
    return pageReturn(request, BAN_HANG)


def dichvu(request):
    return pageReturn(request, DICH_VU)


def phutung(request):
    return pageReturn(request, PHU_TUNG)


def laixeantoan(request):
    return pageReturn(request, LAI_XE_AN_TOAN)


def thanhvien(request):
    return pageReturn(request, THANH_VIEN)


def tintuc(request):
    return pageReturn(request, TIN_TUC)


def tuyendung(request):
    return pageReturn(request, TUYEN_DUNG)
