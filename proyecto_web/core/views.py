from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'core/index.html')

def carrito(request):

    return render(request, 'core/carrito.html')

def ingresarRegistro(request):

    return render(request, 'core/ingresar-registro.html')    

def ingresar(request):

    return render(request, 'core/ingresar.html')