from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Plantas
from .serializers import PlantasSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated,))
def lista_plantas(request):

    #Lista todas las plantas
    if request.method == 'GET':
        plants = Plantas.objects.all()
        serializer = PlantasSerializer(plants, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlantasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_plantas(request, id):

    #get, update y delete 
    try:
        plants = Plantas.objects.get(idPlanta=id)
    except plants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    if request.method == 'GET':
        serializer = PlantasSerializer(plants)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PlantasSerializer(plants, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        plants.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
