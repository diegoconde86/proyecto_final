from django.shortcuts import render
from time import strftime
from django.http import HttpResponse
from App.forms import MascotaFormulario, ClienteFormulario, UserRegisterForm1, VeterinarioFormulario, UserEditForm, ArticuloFormulario
from App.models import Articulo, Mascota, Cliente, Veterinario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required    #@login_required
from datetime import date, datetime

# Create your views here.
def inicio(request):

    return render(request, 'App/inicio.html')

def mascota(request):
    return render(request, 'App/mascota.html')

def cliente(request):
    return render(request, 'App/cliente.html')

def veterinario(request):
    return render(request, 'App/veterinario.html')


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


'''def buscar(request):

    if request.GET['nombre']:
        nombre_mascota = request.GET['nombre']
        mascotas = Mascota.objects.filter(nombre__icontains = nombre_mascota) # una lista con la busqueda correspondiente

        return render(request, 'App/resultadosBusqueda.html', {'mascotas':mascotas})
    else:
        return render(request, 'App/busquedaMascota.html', {'errors':'No ingresaste ningún nombre de mascota'})'''

# Agregado: DC - LOGIN --------------------------------------------------------


def login_request(request):
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

def editarperfil(request):
    usuario=request.user
    if request.method=="POST":
        formulario= UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            print("ESTOY")
            print(informacion['password1'])
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request, 'App/inicio.html', {'usuario':usuario, 'mensaje': 'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'App/editarperfil.html', {'formulario':formulario, 'usuario':usuario.username})    

    # CRUD NUESTRAS MASCOTAS --------------------------------------------------------


@login_required
def mascotaFormulario(request):
    autor = request.user.username
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        miFormulario = MascotaFormulario(request.POST, request.FILES)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            mascota = Mascota(nombre = informacion['nombre'], edad = informacion['edad'], tipo = informacion['tipo'], imagen=informacion['imagen'], autor=autor, fecha=fecha)
            mascota.save()

            return render(request, 'App/inicio.html')
        
    else:
        miFormulario= MascotaFormulario()

    return render(request, 'App/mascotaFormulario.html', {'miFormulario':miFormulario} )

@login_required
def nuestrasmascotas(request):
    mascotas= Mascota.objects.all().order_by('id').reverse()
    contexto={"mascotas":mascotas}
    return render(request, "App/nuestrasmascotas.html",contexto)

@login_required
def eliminarmascota(request, nombre_mascota):
    mascotas= Mascota.objects.get(nombre=nombre_mascota)
    mascotas.delete()
    mascotas= Mascota.objects.all()
    contexto={"mascotas":mascotas}
    return render(request, "App/nuestrasmascotas.html",contexto)

@login_required
def editarmascota(request,nombre_mascota):
    autor = request.user.username
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mascotas= Mascota.objects.get(nombre=nombre_mascota)
    if request.method == "POST":
        form = MascotaFormulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            mascotas.nombre = info['nombre']
            mascotas.edad= info["edad"]
            mascotas.tipo= info["tipo"]
            mascotas.autor= info["autor"]
            mascotas.fecha= fecha
            mascotas.save()
            return render(request,"App/inicio.html")
    else:
        form= MascotaFormulario(initial={"nombre":mascotas.nombre, "edad":mascotas.edad, "tipo":mascotas.tipo, "autor":mascotas.autor, "fecha":mascotas.fecha})
    return render(request, "App/editarmascota.html",{"formulario":form, "nombre_mascota":nombre_mascota})

def buscar(request):
    if request.GET["nombre"]:
        nombre_mascota= request.GET["nombre"]
        mascotas = Mascota.objects.filter(nombre__icontains = nombre_mascota).order_by('id').reverse()
        contexto={"mascotas":mascotas,"mensaje":f"Resultados de la Busqueda {nombre_mascota}" }
        return render(request, "App/nuestrasmascotas.html", contexto)
    else:
        return render(request, "App/nuestrasmascotas.html", {"mensaje":" No se ingreso ningun nombre."})

# CRUD ARTICULOS --------------------------------------------------------

@login_required
def articulos(request):
    articulos= Articulo.objects.all().order_by('id').reverse()
    contexto={"articulos":articulos}
    return render(request, "App/articulos.html",contexto)

@login_required
def articuloFormulario(request):
    autor = request.user.username
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        miFormulario = ArticuloFormulario(request.POST, request.FILES)
        if miFormulario.is_valid:
            informacion =  miFormulario.cleaned_data
            articulo = Articulo(titulo = informacion['titulo'], subtitulo = informacion['subtitulo'], cuerpo = informacion['cuerpo'], autor=autor, fecha=fecha, editado = informacion['editado'], imagen=informacion['imagen'],  )
            articulo.save()

            return render(request, 'App/inicio.html')
        
    else:
        miFormulario= ArticuloFormulario()

    return render(request, 'App/articuloFormulario.html', {'miFormulario':miFormulario} )

@login_required
def editararticulo(request,id_art):
    imagen = Articulo.objects.get(id=id_art)
    #fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    articulo= Articulo.objects.get(id=id_art)
    if request.method == "POST":
        form = ArticuloFormulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            articulo.titulo = info['titulo']
            articulo.subtitulo= info["subtitulo"]
            articulo.cuerpo= info["cuerpo"]
            articulo.autor= info["autor"]
            articulo.fecha= info["fecha"]
            articulo.editado= info["editado"]
            articulo.imagen= info["imagen"]
            articulo.save()
            return render(request,"App/inicio.html")
    else:
        form= ArticuloFormulario(initial={"titulo":articulo.titulo, "subtitulo":articulo.subtitulo, "cuerpo":articulo.cuerpo, "autor":articulo.autor, "fecha":articulo.fecha
        , "editado":articulo.editado, "imagen":imagen.imagen})
    return render(request, "App/editararticulo.html",{"miFormulario":form, "id_art":id_art})   

def buscararticulo(request):
    
    if request.GET["titulo"]:
        print("SII")
        titulo_articulo= request.GET["titulo"]
        articulo = Articulo.objects.filter(titulo__icontains = titulo_articulo).order_by('id').reverse()
        contexto={"articulos":articulo,"mensaje":f"Resultados de la Busqueda {titulo_articulo}" }
        return render(request, "App/articulos.html", contexto)
    else:
        return render(request, "App/articulos.html", {"mensaje":" No se ingreso ninguna descripción."})

@login_required
def leerarticulo(request,id_art):
    articulo = Articulo.objects.filter(id=id_art)
    print(request.method)
    if request.method == "POST":
        contexto={"articulos":articulo}
        return render(request, "App/leerarticulo.html",contexto)
    else:
        contexto={"articulos":articulo}
    return render(request, "App/leerarticulo.html",contexto)    
    