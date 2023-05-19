from django.contrib import admin
from django.urls import path

from webapp.views import editar, despedirse, inicio, registro, persona_list, persona_register,editar,eliminar

urlpatterns = [
    path('',inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('registro/', persona_register, name='registro'),
    path('personas/', persona_list, name='persona_list'),
    path('editar/<int:id>/', editar, name='editar_persona'),
    path('eliminar/<int:id>/', eliminar, name='eliminar_persona'),
    path('despedida/',despedirse),

]
