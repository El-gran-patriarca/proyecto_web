from django.urls import path
from .views import home, ingresar, carrito, ingresarRegistro, clima

urlpatterns = [
    path('', home, name="home"),
    path('ingresar', ingresar, name="ingresar"),
    path('carrito', carrito, name="carrito"),
    path('clima', clima, name="clima"),
    path('ingresarRegistro', ingresarRegistro, name="ingresarRegistro")
]


