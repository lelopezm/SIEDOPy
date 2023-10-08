from rest_framework import viewsets
from .models import Euler_nm
from .serializer import EulerNMSerializer

class EulerNMView(viewsets.ModelViewSet):
    ''' Class View is used to define easily CRUD operations. '''

    queryset = Euler_nm.objects.all()
    serializer_class = EulerNMSerializer
