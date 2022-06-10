
from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Plantas

class PlantasForm(ModelForm):

    class Meta:
        model = Plantas
        fields = ['idPlanta','tipoPlanta','nombrePlanta','categoria']
