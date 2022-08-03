from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField,RichTextFormField

class MascotaFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    tipo = forms.CharField()
    #imagen = forms.ImageField()
    autor = forms.CharField(max_length=60)
    fecha = forms.DateTimeField()

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class VeterinarioFormulario(forms.Form):
    nombre = forms.CharField()
    especialidad = forms.CharField()

class UserRegisterForm1(UserCreationForm):
    email=forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


