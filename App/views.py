from django.shortcuts import render
from django.http import HttpResponse
from App.forms import MascotaFormulario, ClienteFormulario, VeterinarioFormulario
from App.models import Mascota, Cliente, Veterinario

# Create your views here.
def inicio(request):

    return render(request, 'App/inicio.html')

def mascota(request):
    return render(request, 'App/mascota.html')

def cliente(request):
    return render(request, 'App/cliente.html')

def veterinario(request):
    return render(request, 'App/veterinario.html')

def mascotaFormulario(request):
    if request.method == 'POST':
        miFormulario = MascotaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            mascota = Mascota(nombre = informacion['nombre'], edad = informacion['edad'], tipo = informacion['tipo'])
            mascota.save()

            return render(request, 'App/inicio.html')
        
    else:
        miFormulario= MascotaFormulario()

    return render(request, 'App/mascotaFormulario.html', {'miFormulario':miFormulario} )

def clienteFormulario(request):
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            cliente = Cliente(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            cliente.save()

            return render(request, 'App/inicio.html')
        
    else:
        miFormulario= ClienteFormulario()

    return render(request, 'App/clienteFormulario.html', {'miFormulario':miFormulario} )

def veterinarioFormulario(request):
    if request.method == 'POST':
        miFormulario = VeterinarioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            veterinario = Veterinario(nombre = informacion['nombre'], especialidad = informacion['especialidad'])
            veterinario.save()

            return render(request, 'App/inicio.html')
        
    else:
        miFormulario= VeterinarioFormulario()

    return render(request, 'App/veterinarioFormulario.html', {'miFormulario':miFormulario} )

def busquedaMascota(request):
    return render(request, 'App/busquedaMascota.html')


def buscar(request):

    if request.GET['nombre']:
        nombre_mascota = request.GET['nombre']
        mascotas = Mascota.objects.filter(nombre__icontains = nombre_mascota) # una lista con la busqueda correspondiente

        return render(request, 'App/resultadosBusqueda.html', {'mascotas':mascotas})
    else:
        return render(request, 'App/busquedaMascota.html', {'errors':'No ingresaste ningún nombre de mascota'})

