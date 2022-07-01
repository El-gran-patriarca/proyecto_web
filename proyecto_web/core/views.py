from django.shortcuts import render , redirect
from .models import Plantas, Usuario 
from django.contrib.auth.forms import UserCreationForm
import requests
from rest_framework import status

# Create your views here.

def home(request):

    return render(request, 'core/index.html')

def carrito(request):

    return render(request, 'core/carrito.html')

def ingresarRegistro(request):

    return render(request, 'core/ingresar-registro.html')    

def ingresar(request):
    datos = {}
    if request.method == 'POST':
        username = request.POST.get('joinusUser')
        password = request.POST.get('joinusPassword')

        jsonPost = {
            "username": username,
            "password": password
        }

        endpoint = 'http://127.0.0.1:8000/api/login'#?user={username}&passw={password}
        url = endpoint.format(username=username, password=password)
        print('ingreso print')
        response = requests.post(endpoint, json=jsonPost)
        print(response.json())
        if response.status_code == status.HTTP_200_OK:
            
            resultado = response.json()
            return render(request, 'core/vista_usuario.html')
        
        datos['message'] = response.json()

    return render(request, 'core/ingresar.html', datos)
    
def clima(request):

    return render(request, 'core/clima.html')

def perfilUsuario(request):
    #http://127.0.0.1:8000/api/lista_plantas
    endpoint = 'http://127.0.0.1:8000/api/lista_plantas'
    url = endpoint.format(idPlanta=3)

    response = requests.get(endpoint)
    resultado = response.json()

    datos ={
        'plantas' : resultado
    }
    return render(request, 'core/perfil_usuario.html' , datos)    



def growAdmin(request):

    plantas = Plantas.objects.all()

    datos ={
        'plantas' : plantas
    }
    return render(request, 'core/grow_admin.html' , datos)


def registro(request):

    usuario = Usuario.objects.all()

    datos ={
        'usuario' : usuario
    }
    return render(request, 'core/ingresar-registro.html' , datos)

def formPlantas(request):
    datos = {
        'form': PlantasForm()
    }
    
    if request.method == 'POST':
        formulario = PlantasForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['message'] = 'Guardado correctamente'
        else:
            datos['message'] = 'Hubo un problema'
    
    return render(request, 'core/form_plantas.html', datos) 

def usuario(request):

    return render(request, 'core/vista_usuario.html')    

def formModPlantas(request , id):
    
    plantas = Plantas.objects.get(idPlanta= id)

    datos = {
        'form' : PlantasForm (instance= plantas)
    }

    if request.method == 'POST':

        formulario = PlantasForm(data=request.POST, instance=plantas)
    
        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = "Modificados correctamente"
    
    return render(request, 'core/form_mod_plantas.html', datos)

def formDelPlantas(request, id):

    plantas = Plantas.objects.get(idPlanta=id)

    plantas.delete()
    return redirect(to ="grow_admin")

   


