
from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Usuario,Plantas

class PlantasForm(ModelForm):

    class Meta:
        model = Plantas
        fields = ['idPlanta','tipoPlanta','nombrePlanta','imagenPlanta','costoPlanta','categoria']


class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['Usuario','contraseña']      
