from django.core.validators import EmailValidator
from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, validators=[EmailValidator])
    edad = models.IntegerField(max_length=50)
