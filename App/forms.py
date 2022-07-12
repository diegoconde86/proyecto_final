from django import forms

class MascotaFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    tipo = forms.CharField()

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class VeterinarioFormulario(forms.Form):
    nombre = forms.CharField()
    especialidad = forms.CharField()