from rest_framework import viewsets, permissions, filters
from .models import Superhero, Supervillain, Location, Character
from .serializers import SuperheroSerializer, SupervillainSerializer, LocationSerializer, CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all().prefetch_related(
        'location').order_by('superhero_name')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['publisher']


class SuperheroViewSet(viewsets.ModelViewSet):
    serializer_class = SuperheroSerializer
    queryset = Superhero.objects.all().prefetch_related(
        'location').order_by('superhero_name')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['publisher']


class SupervillainViewSet(viewsets.ModelViewSet):
    serializer_class = SupervillainSerializer
    queryset = Supervillain.objects.all().prefetch_related(
        'location').order_by('superhero_name')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['publisher']


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
