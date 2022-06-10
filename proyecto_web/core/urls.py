from django.urls import path
from .views import home, ingresar, carrito, ingresarRegistro, clima, growAdmin, from_plantas

urlpatterns = [
    path('', home, name="home"),
    path('ingresar', ingresar, name="ingresar"),
    path('carrito', carrito, name="carrito"),
    path('clima', clima, name="clima"),
    path('grow-admin', growAdmin, name="grow-admin"),
    path('from_plantas', from_plantas, name="from_plantas"),
    path('ingresarRegistro', ingresarRegistro, name="ingresarRegistro")
]


