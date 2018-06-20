from ..models import Person
from rest_framework import serializers, viewsets
from rest_framework import permissions


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    #permission_classes = [permissions.IsAuthenticated]
