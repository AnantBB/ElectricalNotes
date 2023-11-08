from django.urls import path
from . import views

app_name = 'Elements'

urlpatterns = [
    path('', views.home, name='home'),    
    path('res_info', views.res_info, name='res_info'),
    path('indc_info', views.indc_info, name='indc_info'),
    path('res_calc', views.res_calc, name='res_calc'),
    path('res_grph', views.res_grph, name='res_grph'),    
    path('help', views.help, name='help')
]