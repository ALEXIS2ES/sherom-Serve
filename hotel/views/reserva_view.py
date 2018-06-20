from ..models.reserva import Reserva
from rest_framework import serializers, viewsets
from rest_framework import permissions


class ReservaSerializer(serializers.ModelSerializer):
    nombre_cliente = serializers.SerializerMethodField()

    class Meta:
        model = Reserva
        fields = '__all__'

    def get_nombre_cliente(self, obj):
        return "%s %s %s" % (obj.cliente.nombre,
                             obj.cliente.apellido_paterno,
                             obj.cliente.apellido_materno)


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
