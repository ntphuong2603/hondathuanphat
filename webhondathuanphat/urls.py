from django.urls import path
from . import views


urlpatterns = [
    path('', views.trangchu, name='trangchu'),
	path('phutung', views.phutung, name='phutung'),
	path('laixeantoan', views.laixeantoan, name='laixeantoan'),
	path('tintuc', views.tintuc, name='tintuc'),
	path('tuyendung', views.tuyendung, name='tuyendung'),    
]
