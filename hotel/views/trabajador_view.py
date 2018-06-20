from ..models.trabajador import Trabajador
from rest_framework import serializers, viewsets


class TrabajadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trabajador
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    #permission_classes = [permissions.IsAuthenticated]
