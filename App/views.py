from django.shortcuts import render
from django.http import HttpResponse
from App.forms import MascotaFormulario, ClienteFormulario, UserRegisterForm1, VeterinarioFormulario
from App.models import Mascota, Cliente, Veterinario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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

def nosotros(request):
    return render(request, 'App/nosotros.html')


def buscar(request):

    if request.GET['nombre']:
        nombre_mascota = request.GET['nombre']
        mascotas = Mascota.objects.filter(nombre__icontains = nombre_mascota) # una lista con la busqueda correspondiente

        return render(request, 'App/resultadosBusqueda.html', {'mascotas':mascotas})
    else:
        return render(request, 'App/busquedaMascota.html', {'errors':'No ingresaste ningún nombre de mascota'})

# Agregado: DC - LOGIN --------------------------------------------------------


def login_request(request):
    print("HOLA")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            usu= request.POST['username']
            contra= request.POST['password']
            usuario=authenticate(username=usu,password=contra)
          
            if usuario is not None:
                login(request,usuario)
                return render(request,"App/inicio.html", {'form':form,"mensaje":f"Bienvenido {usuario}."})
            else:
                return render(request,"App/login.html", {'form':form,"mensaje":"Error, datos incorrectos."})
        else:
                return render(request,"App/login.html", {"mensaje":"Error, Formulario erroneo."})
    form=AuthenticationForm()
    return render(request,"App/login.html", {'form':form})

def register(request):
    if request.method == 'POST':
        form= UserRegisterForm1(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request,"App/inicio.html", {'form':form,"mensaje":f"Usuaio Creado.{username}"})
    else:
        form= UserRegisterForm1()
    return render(request,"App/register.html", {'form':form})

    