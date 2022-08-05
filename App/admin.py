from django.contrib import admin
from App.models import Veterinario, Cliente, Mascota, Articulo

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(Veterinario)

