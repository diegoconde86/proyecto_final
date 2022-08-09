from django.shortcuts import render
from time import strftime
from django.http import HttpResponse
from App.forms import MascotaFormulario, ClienteFormulario, UserRegisterForm1, VeterinarioFormulario, UserEditForm, ArticuloFormulario, Avatar_Formulario
from App.models import Articulo, Avatar, Mascota, Cliente, Veterinario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required    #@login_required
from datetime import date, datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your views here.
def inicio(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    return render(request, 'App/inicio.html',{'avatar':avatar})

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
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    return render(request, 'App/nosotros.html',{'avatar':avatar})

# Agregado: DC - LOGIN --------------------------------------------------------


def login_request(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            usu= request.POST['username']
            contra= request.POST['password']
            usuario=authenticate(username=usu,password=contra)
          
            if usuario is not None:
                login(request,usuario)
                return render(request,"App/inicio.html", {'avatar':avatar,'form':form,"mensaje":f"Bienvenido {usuario}."})
            else:
                return render(request,"App/login.html", {'form':form,"mensaje":"Error, datos incorrectos."})
        else:
                return render(request,"App/login.html", {"mensaje":"Error, Formulario erroneo."})
    form=AuthenticationForm()
    return render(request,"App/login.html", {'avatar':avatar,'form':form})


def register(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    autor = request.user.username
    if request.method == 'POST':
        form= UserRegisterForm1(request.POST)
        img= Avatar_Formulario(request.POST, request.FILES)
        if form.is_valid() and img.is_valid():
            username=form.cleaned_data["username"]
            avatar_info=img.cleaned_data
            form.save()
            id_nuevo = User.objects.latest('id') #obtengo el ultimo id, para cargar la imagen
            print(id_nuevo.id)
            avatar_form = Avatar(imagen=avatar_info["imagen"],user_id=id_nuevo.id)
            avatar_form.save()
            return render(request,"App/inicio.html", {'avatar':avatar,'form':form,'avatar_form':avatar_form,"mensaje":f"Usuario Creado.{username}"})
    else:
        form= UserRegisterForm1()
        avatar_form = Avatar_Formulario()
    return render(request,"App/register.html", {'avatar':avatar,'form':form ,'avatar_form':avatar_form})

def editarperfil(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    autor = request.user.username
    usuario=request.user
    img_actual= Avatar.objects.get(user_id=request.user.id)
    if request.method=="POST":
        formulario= UserEditForm(request.POST, instance=usuario)
        img= Avatar_Formulario(request.POST, request.FILES)
        if formulario.is_valid() and img.is_valid():
            informacion=formulario.cleaned_data
            avatar_info=img.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            img_actual.imagen=avatar_info["imagen"]
            img_actual.save()
            return render(request, 'App/inicio.html', {'avatar':avatar,'form':usuario,'avatar_form':img, 'mensaje': 'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
        #img= Avatar.objects.get(user_id=request.user.id)
        img= Avatar_Formulario(initial={"imagen":img_actual.imagen})
    return render(request, 'App/editarperfil.html', {'avatar':avatar,'formulario':formulario,'avatar_form':img, 'usuario':usuario.username})    

    # CRUD NUESTRAS MASCOTAS --------------------------------------------------------


@login_required
def mascotaFormulario(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    autor = request.user.username
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        miFormulario = MascotaFormulario(request.POST, request.FILES)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            mascota = Mascota(nombre = informacion['nombre'], edad = informacion['edad'], tipo = informacion['tipo'], imagen=informacion['imagen'], autor=autor, fecha=fecha)
            mascota.save()

            #return render(request, 'App/inicio.html')
            mascotas= Mascota.objects.all().order_by('id').reverse()
            contexto={'avatar':avatar,"mascotas":mascotas}
            return render(request, "App/nuestrasmascotas.html",contexto)
        
    else:
        miFormulario= MascotaFormulario()

    return render(request, 'App/mascotaFormulario.html', {'avatar':avatar,'miFormulario':miFormulario} )

@login_required
def nuestrasmascotas(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    mascotas= Mascota.objects.all().order_by('id').reverse()
    contexto={'avatar':avatar,"mascotas":mascotas}
    return render(request, "App/nuestrasmascotas.html",contexto)

@login_required
def eliminarmascota(request, nombre_mascota):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    mascotas= Mascota.objects.get(nombre=nombre_mascota)
    mascotas.delete()
    mascotas= Mascota.objects.all()
    contexto={'avatar':avatar,"mascotas":mascotas}
    return render(request, "App/nuestrasmascotas.html",contexto)

@login_required
def editarmascota(request,nombre_mascota):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    autor = request.user.username
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mascotas= Mascota.objects.get(nombre=nombre_mascota)
    if request.method == "POST":
        form = MascotaFormulario(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            mascotas.nombre = info['nombre']
            mascotas.edad= info["edad"]
            mascotas.tipo= info["tipo"]
            mascotas.autor= info["autor"]
            mascotas.fecha= fecha
            mascotas.imagen = info['imagen']
            mascotas.save()
            #return render(request,"App/inicio.html")
            mascotas= Mascota.objects.all().order_by('id').reverse()
            contexto={'avatar':avatar,"mascotas":mascotas}
            return render(request, "App/nuestrasmascotas.html",contexto)
    else:
        form= MascotaFormulario(initial={"nombre":mascotas.nombre, "edad":mascotas.edad, "tipo":mascotas.tipo, "autor":mascotas.autor, "fecha":mascotas.fecha})
    return render(request, "App/editarmascota.html",{'avatar':avatar,"formulario":form, "nombre_mascota":nombre_mascota})

def buscar(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    if request.GET["nombre"]:
        nombre_mascota= request.GET["nombre"]
        mascotas = Mascota.objects.filter(nombre__icontains = nombre_mascota).order_by('id').reverse()
        contexto={'avatar':avatar,"mascotas":mascotas,"mensaje":f"Resultados de la Busqueda {nombre_mascota}" }
        return render(request, "App/nuestrasmascotas.html", contexto)
    else:
        return render(request, "App/nuestrasmascotas.html", {'avatar':avatar,"mensaje":" No se ingreso ningun nombre."})

# CRUD ARTICULOS --------------------------------------------------------


def articulos(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    articulos= Articulo.objects.all().order_by('id').reverse()
    contexto={'avatar':avatar,"articulos":articulos}
    return render(request, "App/articulos.html",contexto)

@login_required
def articuloFormulario(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    autor = request.user.username
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        miFormulario = ArticuloFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            informacion =  miFormulario.cleaned_data
            articulo = Articulo(titulo = informacion['titulo'], subtitulo = informacion['subtitulo'], cuerpo = informacion['cuerpo'], autor=autor, fecha=fecha, editado = autor, imagen=informacion['imagen'],  )
            articulo.save()

            #return render(request,"App/articulos.html")
            articulos= Articulo.objects.all().order_by('id').reverse()
            contexto={'avatar':avatar,"articulos":articulos}
            return render(request, "App/articulos.html",contexto)
        
    else:
        miFormulario= ArticuloFormulario()

    return render(request, 'App/articuloFormulario.html', {'avatar':avatar,'miFormulario':miFormulario} )

@login_required
def editararticulo(request,id_art):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    imagen = Articulo.objects.get(id=id_art)
    autor = request.user.username
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    articulo= Articulo.objects.get(id=id_art)
    if request.method == "POST":
        form = ArticuloFormulario(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            articulo.titulo = info['titulo']
            articulo.subtitulo= info["subtitulo"]
            articulo.cuerpo= info["cuerpo"]
            articulo.autor= autor
            articulo.fecha= info["fecha"]
            articulo.editado= autor
            articulo.imagen= info["imagen"]
            articulo.save()
            #return render(request,"App/articulos.html")
            articulos= Articulo.objects.all().order_by('id').reverse()
            contexto={'avatar':avatar,"articulos":articulos}
            return render(request, "App/articulos.html",contexto)
    else:
        form= ArticuloFormulario(initial={"titulo":articulo.titulo, "subtitulo":articulo.subtitulo, "cuerpo":articulo.cuerpo, "autor":articulo.autor, "fecha":articulo.fecha
        , "editado":articulo.editado, "imagen":imagen.imagen})
    return render(request, "App/editararticulo.html",{'avatar':avatar,"miFormulario":form, "id_art":id_art})   

@login_required
def buscararticulo(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    if request.GET["titulo"]:
        print("SII")
        titulo_articulo= request.GET["titulo"]
        articulo = Articulo.objects.filter(titulo__icontains = titulo_articulo).order_by('id').reverse()
        contexto={'avatar':avatar,"articulos":articulo,"mensaje":f"Resultados de la Busqueda {titulo_articulo}" }
        return render(request, "App/articulos.html", contexto)
    else:
        return render(request, "App/articulos.html", {'avatar':avatar,"mensaje":" No se ingreso ninguna descripción."})


def leerarticulo(request,id_art):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    articulo = Articulo.objects.filter(id=id_art)
    print(request.method)
    if request.method == "POST":
        contexto={'avatar':avatar,"articulos":articulo}
        return render(request, "App/leerarticulo.html",contexto)
    else:
        contexto={'avatar':avatar,"articulos":articulo}
    return render(request, "App/leerarticulo.html",contexto)    

@login_required
def eliminararticulo(request, id_art):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    articulo= Articulo.objects.get(id=id_art)
    articulo.delete()
    articulo= Articulo.objects.all()
    contexto={'avatar':avatar,"articulos":articulo}
    return render(request, "App/articulos.html",contexto)

@login_required   
def chat(request):
    avatar = imagenAvatar(Avatar.objects.filter(user=request.user.id))
    users = User.objects.all()
    contexto={'avatar':avatar,"chats":users}
    return render(request,"App/chat.html",contexto)


# AVATAR --------------------------------------------------------

def imagenAvatar(a,**kwargs):
    avatares = a
    if avatares:                                  
        return (avatares[0].imagen.url)
    else:
        no_avatar = '/avatares/default.jpg'
        return (no_avatar)