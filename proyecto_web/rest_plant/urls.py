from django.urls import path
from rest_plant.views import lista_plantas, detalle_plantas
from rest_plant.viewslogin import login


urlpatterns = [
    path('lista_plantas', lista_plantas, name="lista_plantas"),
    path('detalle_plantas/<id>', detalle_plantas, name="detalle_plantas"),
    path('login', login, name="login"),
]