from django.urls import path
from . import viewsDichvu as dichvu


urlpatterns = [
    path('hensuachua', dichvu.henlichsuachua, name='henlichsuachua'),
]
