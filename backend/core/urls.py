from rest_framework import routers
from django.urls import path, include
# from rest_framework.documentation import include_docs_urls
from .views import *

router = routers.DefaultRouter()

# Registro de rutas para el modelo Euler_NM
router.register(r'euler', Euler_NMView, 'euler')

urlpatterns = [
    path('', include(router.urls)),
    # path('docs/', include_docs_urls(title='Core API Docs')),
]
