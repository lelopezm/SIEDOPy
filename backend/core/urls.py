from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'euler', EulerNMView, 'euler')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Tasks API Docs')),
]