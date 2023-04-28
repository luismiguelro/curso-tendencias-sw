from django.http import  HttpResponse
from django.shortcuts import render
from personas.models import Persona
# Create your views here.

def bienvenido(request):
    num_personas= Persona.objects.count()
    personas = Persona.objects.all()
    DicMensajes={'msg1':'Valor mensaje 1'}
    # Renderizar html en django
    return render(request,'EstudiantesTdeA.html',{'no_personas':num_personas,'personas':personas})

def despedirse(request):
    return HttpResponse('Despedida desde Django')

# inicio
def inicio(request):
    DicMensajes={'msg1':'Que me ves marrana'}
    return (render(request,'inicio.html',DicMensajes))

def contacto(request):
    return (render(request,'contacto.html'))