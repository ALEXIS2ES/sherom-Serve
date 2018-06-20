from ..models.tipoHabitacion import Tipo_Habitacion
from rest_framework import serializers, viewsets
from rest_framework import permissions


class Tipo_HabitacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipo_Habitacion
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class Tipo_HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Habitacion.objects.all()
    serializer_class = Tipo_HabitacionSerializer
    #permission_classes = [permissions.IsAuthenticated]
