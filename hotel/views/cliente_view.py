from ..models.cliente import Cliente
from rest_framework import serializers, viewsets
from rest_framework import permissions


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [permissions.IsAuthenticated]
