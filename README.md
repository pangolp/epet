# Epet 20 - Neuquén

Saludos y bienvenidos. El repositorio que estas consultando actualmente es un proyecto desarrollado en **Django 2.2**, que tiene como objetivo, que los alumnos de 5 y 6 año, aprendan a utilizar la herramienta, pero a su vez, brindar suporte a algunas cosas que creemos pueden resolver problemas actuales.

# Instalación

```sh
$ pip install Django==2.2
$ pip install Pillow # Para el manejo de imágenes en los formularios.
```

Se recomienda siempre revisar el fichero requirements.txt el cual va a contener un listado de todas las librerías utilizadas en el desarrollo con sus respectivas versiones.

### Documentación

* [Django 2.2](https://docs.djangoproject.com/en/2.2/)
* [Bootstrap](https://getbootstrap.com/)
* [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)

Recuerden generar y aplicar migraciones.

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Servidor de desarrollo, a través del comando:

```sh
$ python manage.py runserver
```