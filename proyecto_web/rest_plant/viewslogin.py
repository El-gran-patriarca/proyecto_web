from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
#@permission_classes((IsAuthenticated,))
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido", status=status.HTTP_400_BAD_REQUEST)
    # validamos la pass
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Password incorrecta", status=status.HTTP_400_BAD_REQUEST)

    #permite crear o recuperar el token
    token, created = Token.objects.get_or_create(user=user)
    #print(token.key)
    return Response(token.key, status=status.HTTP_200_OK)   

def register(request):
    try:

        data = JSONParser().parse(request)

        username = data['username']
        email = data['email']
        password = data['password']
        
        
        user = User.objects.create_user(username, email, password)

        user.save()           
        return Response(True) 
        
    except:
        return Response(False)

def register_page(request):

    register_form = UserCreationForm()

    return render(request, 'core/ingresar-registro.html', {  
        'title' : 'Registro',
        'register_form' : register_form 
    })   