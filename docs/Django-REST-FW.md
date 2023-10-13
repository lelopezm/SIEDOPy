# Django REST Notes
## Instalación de Django REST Framework
Para comenzar a trabajar con Django REST Framework, es necesario seguir estos pasos:

1. __Instalar Django REST Framework:__ Primero, instala Django REST Framework a través del archivo de requerimientos `requirements.txt` del proyecto.

2. __Agregar la aplicación Django REST Framework:__ En el archivo `settings.py` del proyecto Django, en la sección `INSTALLED_APPS`, asegúrate de agregar `'rest_framework'` y `'corsheaders'` y `'coreapi'` como aplicaciones instaladas.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
]
```

### Configuración de CORS
__Configurar CORS:__ Para permitir el acceso a la API desde otros dominios, debes configurar CORS en el mismo archivo `settings.py`. Agrega el middleware de CORS en la sección `MIDDLEWARE` y configura las opciones según tus necesidades.
```
python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
```

Puedes configurar CORS de dos maneras:

1. __Permitir todos los dominios (CORS_ORIGIN_ALLOW_ALL):__ Si deseas permitir todas las solicitudes desde cualquier dominio, agrega la siguiente línea a tu archivo `settings.py`:
```python
CORS_ORIGIN_ALLOW_ALL = True
```
2. __Permitir dominios específicos (CORS_ALLOWED_ORIGINS):__ Si deseas permitir solicitudes solo desde dominios específicos, configura una lista de dominios permitidos en tu archivo `settings.py`.
```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://...",
]
```
## Creación de Modelos y Migraciones
Para crear modelos en Django REST Framework y migrarlos a la base de datos, sigue estos pasos:

1. Define tus modelos en un archivo, este será una clase que hereda `models.Model`, `de la siguiente forma:

```python
from django.db import models


class «nombre_modelo»(models.Model):
    ''' Class Euler_nm is used to approximate. '''
    «nombre_campo»: «tipo_dato» = models.«tipo_dato_model»(«tamaño»)
    # ... otros campos

    def __str__(self):
        return self.name

```
Importado el modelo en `models.py` con el comando `from «ruta» import «nombre_modelo»`, luego migra las tablas correspondientes utilizando los siguientes comandos:
```bash
python manage.py makemigrations «nombre_aplicación»
python manage.py migrate «nombre_aplicación»
```
### Habilitar el Modelo en el Admin
Si deseas ver el modelo generado en el panel de administración de Django, debes realizar los siguientes pasos:

1. Accede al archivo `admin.py` en la aplicación de Django REST Framework.
2. Agrega el siguiente código para registrar el modelo:

```python
from django.contrib import admin
from .models import «nombre_modelo»

admin.site.register(«nombre_modelo»)
```

### Creación de Serializadores
Para definir fácilmente las operaciones CRUD en la API, crea un archivo `serializer.py` en tu aplicación con el siguiente código:

```python
from rest_framework import serializers
from .models import «nombre_modelo»

class «model»Serializer(serializers.ModelSerializer):
    ''' Esta clase de serializador simplifica las operaciones CRUD. '''

    class Meta:
        model = «nombre_modelo»
        fields = '__all__'
        # Opcionalmente, puedes especificar los campos uno por uno en una tupla
```

### Creación de Vistas
En el archivo `views.py` de tu aplicación Django REST Framework, puedes definir las vistas que mostrarán los datos utilizando el siguiente código como ejemplo:

```python
from rest_framework import viewsets
from .models import «nombre_modelo»
from .serializer import «nombre_modelo»Serializer

class «nombre_modelo»View(viewsets.ModelViewSet):
    ''' Esta clase de vista simplifica las operaciones CRUD. '''

    queryset = «nombre_modelo».objects.all()
    serializer_class = «nombre_modelo»Serializer
```

## Configuración de URL
Agrega rutas para tus vistas en el archivo `urls.py` de tu aplicación Django REST Framework.

```python
from rest_framework import routers
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from .views import *

# 1. Crea un objeto router
router = routers.DefaultRouter()

# 2. Registra las vistas con el router
router.register(r'«nombre_modelo»', «nombre_modeloView», '«nombre_modelo»')

# 3. Incluye las rutas del router en urlpatterns
urlpatterns = [
    path('', index, name='index'),
    # Ahora que todas las rutas están configuradas, puedes usar Thunder API para verificar
    path('«nombre_ruta_app»/', include(router.urls)),
    #! Eliminar docs/ si no está COREAPI ¡#
    path('docs/', include_docs_urls(title='«nombre_app» API Docs')),  # Documentación
]
```

Luego, incluye estas rutas en el archivo `urls.py` del proyecto principal de la siguiente manera:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('«nombre_app»/', include('«nombre_app».urls')),
]
```


### Documentación de API
Para acceder a la documentación de tu API, asegúrate de haber agregado `'coreapi'` en tu archivo `settings.py` (Esta puede estar presentando fallos en la versión 3.12 de Django, por lo que se recomienda usar la versión 3.11.2). Luego, agrega la siguiente configuración en el mismo archivo:

```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
```

Puedes acceder a la documentación en http://localhost:8000/«nombre_app»/docs/, donde se encuentran los diferentes endpoints.

Recuerda ajustar los nombres y configuraciones según las necesidades específicas de tu proyecto.