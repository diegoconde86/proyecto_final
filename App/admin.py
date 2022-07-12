from django.contrib import admin
from App.models import Veterinario, Cliente, Mascota

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Cliente)
admin.site.register(Veterinario)

