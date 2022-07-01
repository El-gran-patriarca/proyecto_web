from django.contrib import admin
from .models import Categoria, Plantas ,Usuario

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Plantas)
admin.site.register(Usuario)