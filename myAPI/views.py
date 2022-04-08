from django.shortcuts import render
from rest_framework import viewsets
from . serializers import vehiclsSerializer
from . models import vehicls

class vehiclsviewsets(viewsets.ModelViewSet):
    queryset = vehicls.objects.all().order_by('name')
    serializer_class = vehiclsSerializer

# Create your views here.
