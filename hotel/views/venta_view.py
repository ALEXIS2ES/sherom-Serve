from ..models.venta import Venta
from rest_framework import serializers, viewsets


class VentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venta
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    #permission_classes = [permissions.IsAuthenticated]
