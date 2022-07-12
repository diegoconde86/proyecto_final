from django.urls import path
from App.views import inicio, mascota, cliente,veterinario, mascotaFormulario, clienteFormulario, veterinarioFormulario, busquedaMascota, buscar

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('mascota/', mascota, name='Mascota'),
    path('cliente/', cliente, name='Cliente'),
    path('veterinario/', veterinario, name='Veterinario'),
    path('mascotaFormulario/', mascotaFormulario, name='MascotaFormulario'),
    path('clienteFormulario/', clienteFormulario, name='ClienteFormulario'),
    path('veterinarioFormulario/', veterinarioFormulario, name='VeterinarioFormulario'),
    path('busquedaMascota/', busquedaMascota, name='BusquedaMascota'),
    path('buscar/', buscar),

]
