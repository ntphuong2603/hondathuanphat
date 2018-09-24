from django.urls import path
from ..Folder_views import viewsDichvu as dichvu


urlpatterns = [
    path('hensuachua', dichvu.henlichsuachua, name='henlichsuachua'),
]
