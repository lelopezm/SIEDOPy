from rest_framework import viewsets
from .models import Euler_NM
from .serializer import Euler_NMSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class Euler_NMView(viewsets.ModelViewSet):
    ''' Esta clase de vista simplifica las operaciones CRUD. '''

    queryset = Euler_NM.objects.all()
    serializer_class = Euler_NMSerializer

    @action(detail=True, methods=['get'])


    @action(detail=True, methods=['get'])
    def graph(self, request, pk=None):
        euler_instance = self.get_object()

        euler_instance.generate_graph()

        serializer = self.get_serializer(euler_instance)
        # return Response(serializer.data)
        return Response({'image_url': euler_instance.image_url})

    @action(detail=True, methods=['get'])
    def solve(self, request, pk=None):
        euler_instance = self.get_object()

        data = euler_instance.get_data()
        # serializer = self.get_serializer(euler_instance)

        return Response({'data': data})
