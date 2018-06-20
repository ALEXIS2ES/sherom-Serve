from ..models.docType import Doc_Type
from rest_framework import serializers, viewsets


class Doc_TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc_Type
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class Doc_TypeViewSet(viewsets.ModelViewSet):
    queryset = Doc_Type.objects.all()
    serializer_class = Doc_TypeSerializer
    #permission_classes = [permissions.IsAuthenticated]
