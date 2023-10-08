from rest_framework import serializers
from .models import Euler_nm


class EulerNMSerializer(serializers.ModelSerializer):
    ''' Class Serializer is used to easily define CRUD operations. '''

    class Meta:
        model = Euler_nm
        fields = '__all__'

