from ..models.pago import Forma_de_pago
from rest_framework import serializers, viewsets


class Forma_de_pagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forma_de_pago
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class Forma_de_pagoViewSet(viewsets.ModelViewSet):
    queryset = Forma_de_pago.objects.all()
    serializer_class = Forma_de_pagoSerializer
    #permission_classes = [permissions.IsAuthenticated]
