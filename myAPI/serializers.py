from dataclasses import fields
from rest_framework import serializers
from . models import vehicls

class vehiclsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vehicls
        fields = ('name', 'description')