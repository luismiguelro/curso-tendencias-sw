from django.db import models
from django.forms import forms, ModelForm
from personas.models import Registro

from personas.models import Registro
class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'apellido', 'email','edad']