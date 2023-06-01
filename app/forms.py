from django import forms
from .models import Insumo, Contacto, Tipo_contacto
from datetime import datetime
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxFileSiceValidator

class Tipo_contactoForms(forms.ModelForm):
    nombre = forms.CharField(required=True, min_length=3, max_length=50)

class ContactoForms(forms.ModelForm):
    nombre = forms.CharField(required=True, min_length=3, max_length=50)
    apellido = forms.CharField(required=True, min_length=3, max_length=50)
    asunto = forms.CharField(required=True, min_length=3, max_length=50)
    mensaje = forms.Textarea()

    class Meta:
        model = Contacto
        fields = ["nombre", "apellido", "asunto", "tipo_contacto", "mensaje"]

class InsumoForms(forms.ModelForm):

    nombre = forms.CharField(required=True, min_length=3, max_length=120)
    precio = forms.IntegerField(required=True, min_value=1)
    stock = forms.IntegerField(required=True, min_value=0)
    descripcion = forms.CharField(required=False, min_length=3, max_length=200)
    imagen = forms.ImageField(required=False, validators=[MaxFileSiceValidator(max_file_size=2)])

    class Meta:
        model = Insumo
        fields = ["nombre", "precio", "stock", "descripcion", "imagen"]


class CustomUserCreationForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data["email"]

        if email.lower().endswith("duoc.cl"):
            return email
        elif email.lower().endswith("gmail.com"):
            return email
        elif email.lower().endswith("hotmal.com"):
            return email
        raise ValidationError("El email debe ser valido")
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

        