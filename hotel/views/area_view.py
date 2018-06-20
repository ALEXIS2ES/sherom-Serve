from ..models.area import Area
from rest_framework import serializers, viewsets


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    #permission_classes = [permissions.IsAuthenticated]
