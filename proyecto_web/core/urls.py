from django.urls import path
from .views import home, ingresar, carrito, ingresarRegistro, clima, growAdmin, formPlantas, formModPlantas,formDelPlantas, perfilUsuario, usuario

urlpatterns = [
    path('', home, name="home"),
    path('ingresar', ingresar, name="ingresar"),
    path('carrito', carrito, name="carrito"),
    path('clima', clima, name="clima"),
    path('grow_admin', growAdmin, name="grow_admin"),
    path('form_plantas', formPlantas, name="form_plantas"),
    path('form_mod_plantas/<id>', formModPlantas, name="form_mod_plantas"),
    path('form_del_plantas/<id>', formDelPlantas, name="form_del_plantas"),
    path('ingresarRegistro', ingresarRegistro, name="ingresarRegistro"),
    path('perfilUsuario', perfilUsuario, name="perfilUsuario"),
    path('usuario', usuario, name="usuario"),
]


