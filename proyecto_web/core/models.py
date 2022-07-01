from contextlib import nullcontext
from django.db import models

# Create your models here.
#Modelo para categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

#Modelo para Plantas

class Plantas(models.Model):
    idPlanta = models.IntegerField(primary_key=True ,verbose_name='id planta')
    tipoPlanta = models.CharField(max_length=20 , verbose_name='Tipo de planta')
    nombrePlanta = models.CharField(max_length=50 , verbose_name= 'Nombre planta')
    imagenPlanta = models.CharField(max_length=150 , verbose_name= 'Imagen Planta', null=True)
    costoPlanta = models.IntegerField(max_length=50 , verbose_name= 'Costo planta', null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.idPlanta)
#Modelo para usuario
class Usuario(models.Model):
    Usuario = models.CharField(max_length=20 ,primary_key=True ,verbose_name='User')
    contraseña = models.CharField(max_length=10 ,verbose_name='Contraseña')
    
    def __str__(self):
        return str(self.Usuario)
