from rest_framework import serializers
from .models import Euler_NM


class Euler_NMSerializer(serializers.ModelSerializer):
    ''' Esta clase de serializador simplifica las operaciones CRUD. '''

    class Meta:
        model = Euler_NM
        fields = '__all__'
