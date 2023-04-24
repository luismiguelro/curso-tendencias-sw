from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    # Renderizar html en django
    return render(request,'EstudiantesTdeA.html')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

# inicio
def inicio(request):
    DicMensajes={'msg1':'Que me ves marrana'}
    return (render(request,'inicio.html',DicMensajes))

def contacto(request):
    return (render(request,'contacto.html'))