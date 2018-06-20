from ..models.habitacion import Habitacion
from rest_framework import serializers, viewsets
from rest_framework import permissions


class HabitacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habitacion
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    #permission_classes = [permissions.IsAuthenticated]
