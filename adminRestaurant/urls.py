from django.urls import path
from .views import index,inicio,empleados,empleadosadd,empleados_del,empleados_findEdit,empleadosupdate,inventario,inventarioadd,inventario_del,inventario_findEdit,inventarioupdate,gastos,gastosadd,gastos_del,gastos_finEdit,gastosupdate

urlpatterns =  [
    path ('',inicio,name ='inicio'),
    path ('adminRestaurant/inventario',inventario,name = 'inventario'), #crud inventario
    path ('adminRestaurant/inventario',inventarioadd,name = 'inventarioadd'),
    path ('adminRestaurant/inventario',inventario_del,name = 'inventario_del'),
    path ('adminRestaurant/inventario',inventario_findEdit,name = 'inventario_findEdit'),
    path ('adminRestaurant/inventario',inventarioupdate,name = 'inventarioupdate'),

    path ('adminRestaurant/empleados',empleados,name = 'empleados'),  #crud empleados
    path ('adminRestaurant/empleados',empleadosadd,name = 'empleadosadd'),
    path ('adminRestaurant/empleados',empleados_del,name = 'empleados_del'),
    path ('adminRestaurant/empleados',empleados_findEdit,name = 'empleados_findEdit'),
    path ('adminRestaurant/empleados',empleadosupdate,name = 'empleadosupdate'),

    path ('adminRestaurant/gastos',gastos,name = 'gastos'), #crud gastos
    path ('adminRestaurant/gastos',gastosadd,name = 'gastosadd'),
    path ('adminRestaurant/gastos',gastos_del,name = 'gastos_del'),
    path ('adminRestaurant/gastos',gastos_finEdit,name = 'gastos_finEdit'),
    path ('adminRestaurant/gastos',gastosupdate,name = 'gastosupdate'),


    path ('adminRestaurant/index',index,name = 'index')


]