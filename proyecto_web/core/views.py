from django.shortcuts import render
from .models import Plantas
from .forms import GrowForm

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

def growAdmin(request):

    plantas = Plantas.objects.all()

    datos ={
        'plantas' : plantas
    }
    return render(request, 'core/grow-admin.html' , datos)

def from_plantas(request):
    datos = {
        'form': GrowForm()
    }
    
    if request.method == 'POST':
        formulario = GrowForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['message'] = 'Guardado correctamente'
        else:
            datos['message'] = 'Hubo un problema'
    
    return render(request, 'core/form_plantas.html', datos)