from django.http import  HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegistroForm
from personas.models import Registro


def inicio(request):
    # num_personas= Persona.objects.count()
    # personas = Persona.objects.all()
    # DicMensajes={'msg1':'Valor mensaje 1'}
    # Renderizar html en django
    return (render(request, 'index.html'))
    #return render(request,'EstudiantesTdeA.html',{'no_personas':num_personas,'personas':personas})

def despedirse(request):
    return HttpResponse('Despedida desde Django')



def editar2(request):
    return (render(request,'edit.html'))

def registro(request):
    return (render(request,'registro.html'))


def persona_list(request):
    personas = Registro.objects.all().order_by('id')
    return (render(request,'persona_list.html',{'personas':personas}))


def persona_register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Te has registrado correctamente :)")
            return redirect('persona_list')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

# EDITAR


def editar(request, id):
    persona = get_object_or_404(Registro, id=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=persona)
        if form.is_valid():
            messages.success(request, f"La persona {persona.nombre} ha sido actualizada con éxito.")
            form.save()
            return redirect('persona_list')
    else:
        form = RegistroForm(instance=persona)

    context = {'form': form, 'persona_id': persona.id}
    return render(request, 'edit.html', context)

# Eliminar


def eliminar(request, id):
    persona = get_object_or_404(Registro, id=id)
    if request.method == 'GET':
        # Eliminar el registro
        persona.delete()
        messages.success(request, f"La persona {persona.nombre} ha sido eliminada con éxito.")

    return redirect('persona_list')

