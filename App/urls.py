from django.urls import path
#from App.views import inicio, mascota, cliente,veterinario, mascotaFormulario, clienteFormulario, veterinarioFormulario, busquedaMascota, buscar, login_request, register, nosotros, nuestrasmascotas
from App.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('mascota/', mascota, name='Mascota'),
    path('cliente/', cliente, name='Cliente'),
    path('veterinario/', veterinario, name='Veterinario'),
    path('mascotaFormulario/', mascotaFormulario, name='MascotaFormulario'),
    path('clienteFormulario/', clienteFormulario, name='ClienteFormulario'),
    path('veterinarioFormulario/', veterinarioFormulario, name='VeterinarioFormulario'),
    #path('busquedaMascota/', busquedaMascota, name='BusquedaMascota'),
    path('nosotros/', nosotros, name='Nosotros'),
    path('buscar/', buscar, name='buscar'),
    path('logout/', LogoutView.as_view(template_name='App/logout.html'), name ='logout'),

    #------------------------------------------- URLS LOGIN

    path('login/', login_request, name ='login'),
    path('register/', register, name ='register'),
    path('nuestrasmascotas/', nuestrasmascotas, name='nuestrasmascotas'),
    path('eliminarmascota/<nombre_mascota>', eliminarmascota, name='eliminarmascota'),
    path('editarmascota/<nombre_mascota>', editarmascota, name='editarmascota'),
]