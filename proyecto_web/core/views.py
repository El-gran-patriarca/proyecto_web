from django.shortcuts import render , redirect
from .models import Plantas
from .forms import PlantasForm
from django.contrib.auth.forms import UserCreationForm
import requests

# Create your views here.

def home(request):

    return render(request, 'core/index.html')

def carrito(request):

    return render(request, 'core/carrito.html')

def ingresarRegistro(request):

    return render(request, 'core/ingresar-registro.html')    

def ingresar(request):

    return render(request, 'core/ingresar.html')
    
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

   
def register_page(request):

    register_form = UserCreationForm()

    return render(request, 'core/ingresar.html',{  
        'title' : 'Registro',
        'register_form' : register_form

    })