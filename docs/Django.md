# Django Notes
Primero se debe instalar Django mediante el archivo de requerimientos.
Para conocer las opciones ofrecidas por Django, se debe ejecutar el siguiente comando:
```bash
django-admin help
```

Primero creamos nuestro directorio backend (accedemos con `cd backend/`), donde para crear un proyecto de Django se debe ejecutar el siguiente comando:
```bash
django-admin startproject «nombre_proyecto» .
```
El uso de punto al final del comando (opcional), indica que se debe crear el proyecto en el directorio actual.

Para ejecutar el servidor de Django, se debe ejecutar el siguiente comando:
```bash
python manage.py runserver
```

Ya que estamos en el directorio para crear aplicaciones de Django, se debe ejecutar el siguiente comando:
```bash
python manage.py startapp «nombre_aplicacion»
```
Hay que tener en cuenta que se debe agregar la aplicación creada en el archivo de configuración de Django, `settings.py`, en la sección de aplicaciones (INSTALLED_APPS).
```python
INSTALLED_APPS = [
    ...
    '«nombre_aplicacion»',
]
```

Para crear las migraciones de la aplicación, se debe ejecutar el siguiente comando:
```bash
python manage.py makemigrations
```
Para crear las tablas en la base de datos (inicialmente se tienen las de usuarios), se debe ejecutar el siguiente comando:
```bash
python manage.py migrate
```
Para crear un superusuario, se debe ejecutar el siguiente comando:
```bash
python manage.py createsuperuser
```
| user: siedopy
| pass: uc

Para acceder a la interfaz de administración de Django, se debe acceder a la siguiente dirección:
```bash
http://localhost:8000/admin
```
La cuál por el momento no tiene un usuario creado, por lo que se debe crear uno.
