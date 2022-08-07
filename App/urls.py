from django.urls import path
#from App.views import inicio, mascota, cliente,veterinario, mascotaFormulario, clienteFormulario, veterinarioFormulario, busquedaMascota, buscar, login_request, register, nosotros, nuestrasmascotas
from App.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('mascota/', mascota, name='Mascota'),
    path('cliente/', cliente, name='Cliente'),
    path('veterinario/', veterinario, name='Veterinario'),
    path('clienteFormulario/', clienteFormulario, name='ClienteFormulario'),
    path('veterinarioFormulario/', veterinarioFormulario, name='VeterinarioFormulario'),
    #path('busquedaMascota/', busquedaMascota, name='BusquedaMascota'),
    path('nosotros/', nosotros, name='Nosotros'),
    path('buscar/', buscar, name='buscar'),
    path('logout/', LogoutView.as_view(template_name='App/logout.html'), name ='logout'),

    #------------------------------------------- URLS LOGIN

    path('login/', login_request, name ='login'),
    path('register/', register, name ='register'),
    path('editarperfil/', editarperfil, name='editarperfil'),
    #------------------------------------------- CRUD MASCOTAS

    path('nuestrasmascotas/', nuestrasmascotas, name='nuestrasmascotas'),
    path('eliminarmascota/<nombre_mascota>', eliminarmascota, name='eliminarmascota'),
    path('editarmascota/<nombre_mascota>', editarmascota, name='editarmascota'),
    path('mascotaFormulario/', mascotaFormulario, name='MascotaFormulario'),
    
    #------------------------------------------- CRUD ARTICULOS

    path('articulos/', articulos, name='articulos'),
    path('articuloFormulario/', articuloFormulario, name='articuloFormulario'),
    path('editararticulo/<id_art>', editararticulo, name='editararticulo'),
    path('eliminararticulo/<id_art>', eliminararticulo, name='eliminararticulo'),
    path('buscararticulo/', buscararticulo, name='buscararticulo'),
    path('leerarticulo/<id_art>', leerarticulo, name='leerarticulo'),
    path('chat/', chat, name='chat'),
]