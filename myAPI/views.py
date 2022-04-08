from django.shortcuts import render
from rest_frameworks import viewsets
from . serializers import vehiclsSerializer
from . models import vehicls

class vehiclsviewsets(viewsets.ModelViewSet):
    queryset = vehicls.objects.all().order_by('name')
    serializers_class = vehiclsSerializer

# Create your views here.
