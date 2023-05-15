from rest_framework import viewsets, permissions
from .models import Superhero, Supervillain, Location
from .serializers import SuperheroSerializer, SupervillainSerializer, LocationSerializer
from retrying import retry



class SuperheroViewSet(viewsets.ModelViewSet):  
    serializer_class = SuperheroSerializer
    queryset = Superhero.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SupervillainViewSet(viewsets.ModelViewSet):
    serializer_class = SupervillainSerializer
    queryset = Supervillain.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]