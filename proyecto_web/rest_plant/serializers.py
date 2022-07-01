from rest_framework import serializers
from core.models import Categoria, Plantas

class PlantasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantas
        fields = ['idPlanta','tipoPlanta','nombrePlanta','imagenPlanta','costoPlanta','categoria']