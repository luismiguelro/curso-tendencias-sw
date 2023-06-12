# Proyecto Final del Curso - CRUD con Django & PostgresSQL 🐍
<a
	href="https://www.tdea.edu.co/">
	<img src="https://www.redttu.edu.co/es/wp-content/uploads/2015/12/16.-TDEA.png" alt="Logo Platzi" width="250px" align="right"/>
</a>

Este es el Proyecto Final del Curso de Tendencias en Desarrollo de SW en el Tecnológico de Antioquia

## Objetivos del Proyecto 🎯
Este es un proyecto de ejemplo que muestra cómo crear un CRUD (Create, Read, Update, Delete) utilizando Python, el framework Django y la base de datos PostgreSQL. El objetivo de este proyecto es proporcionar una base sólida para desarrollar aplicaciones web con capacidades CRUD utilizando estas tecnologías.


## Requisitos Previos 📁
- Python 3.x
- Django (se recomienda la versión más reciente)
- PostgreSQL

## Configuración del entorno

1. Crea un entorno virtual (opcional, pero se recomienda) para aislar las dependencias del proyecto:

   ```bash
   $ python3 -m venv myenv
   $ source myenv/bin/activate
   ```

2. Instala Django y las dependencias del proyecto:

   ```bash
   $ pip install django
   $ pip install psycopg2-binary
   ```

## Configuración de la base de datos

1. Crea una base de datos PostgreSQL para el proyecto.

2. Abre el archivo `settings.py` en la carpeta `config` y configura la conexión a la base de datos:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nombre_de_la_base_de_datos',
           'USER': 'usuario',
           'PASSWORD': 'contraseña',
           'HOST': 'localhost',
           'PORT': '',
       }
   }
   ```

   Asegúrate de reemplazar `nombre_de_la_base_de_datos`, `usuario` y `contraseña` con tus propias configuraciones.

## Ejecutar el proyecto

1. Aplica las migraciones para crear las tablas en la base de datos:

   ```bash
   $ python manage.py migrate
   ```

2. Inicia el servidor de desarrollo:

   ```bash
   $ python manage.py runserver
   ```

3. Abre tu navegador y visita `http://localhost:8000`. Verás la página principal de la aplicación.
<div style="text-align: center">
	<img src="./assets/readme/gif-game.gif" alt="Screenshot del juego">
</div>

## Tecnologías utilizadas

<div style="
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	place-items: center;
">
	<img src="https://icon-library.com/images/django-icon/django-icon-0.jpg" alt="django icon"  width="100px">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/800px-Postgresql_elephant.svg.png" alt="postgres icon"  width="100px">
</div>

## Demostracion
![demostracion-crud](https://github.com/luismiguelro/curso-tendencias-sw/assets/101124184/b7a45963-4a7e-42ea-819d-b384c3323841)


## Trabajemos/Aprendamos juntos
<div style="
	display: grid;
	grid-template-columns: repeat(5, 1fr);
	place-items: center;">

 <a href="https://linkedin.com/in/luis-miguel-rodríguez-399292215" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
<a href="https://twitter.com/luismiguelro_" target="_blank">
<img src=https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white alt=twitter style="margin-bottom: 5px;" />
</a>
<a href="https://instagram.com/luismiguelro_" target="_blank">
<img src=https://img.shields.io/badge/instagram-%23000000.svg?&style=for-the-badge&logo=instagram&logoColor=white alt=instagram style="margin-bottom: 5px;" />
</a>  
</div>
