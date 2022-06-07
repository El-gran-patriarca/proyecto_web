from django.urls import path
from .views import home, ingresar, carrito, ingresarRegistro

urlpatterns = [
    path('', home, name="home"),
    path('ingresar', ingresar, name="ingresar"),
    path('carrito', carrito, name="carrito"),
    path('ingresarRegistro', ingresarRegistro, name="ingresarRegistro")
]


