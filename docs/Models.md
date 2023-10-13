# Gestión

Adicionamos métodos en la clase Euler, esta será la encargada de gestionar los datos de entrada (a partir de parámetros) y salida (proceso lógico del algoritmo).

Inyectamos dependencias como:
`import server.settings as settings` para acceso a la ruta del archivo multimedia.

Edición en `settings.py` para adición de:

```python
MEDIA_URL = f'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Creación de la carpeta `media` en el directorio raíz de la aplicación.

Ante modificaciones debemos migrar
python manage.py makemigrations core
python manage.py migrate core

En la vista del modelo, adicionamos el método post:
```python
from rest_framework.decorators import action
from rest_framework.response import Response


@action(detail=True, methods=['post'])
def «nombre_func»(self, request, pk=None):
    «modelo_instance» = self.get_object()

    «modelo_instance».«nombre_func»()

    serializer = self.get_serializer(«modelo_instance»)
    return Response(serializer.data)
```

De forma que podemos acceder a la ruta de la vista del modelo y ejecutar el método post, el cual ejecuta el método de la clase del modelo.

En urls.py del proyecto, debemos poder acceder a la carpeta media, con el código:
```python
# Configuración de URLs para archivos estáticos y multimedia durante el desarrollo
from server import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
```