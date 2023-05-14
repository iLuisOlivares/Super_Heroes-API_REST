from rest_framework import serializers
from .models import Superhero, Supervillain, Location


class SuperheroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superhero
        fields = ('id', 'name', 'alias', 'publisher', 'description', 'location')

class SupervillainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervillain
        fields = ('id', 'name', 'alias', 'publisher', 'description', 'location', 'nemesis')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'city', 'country', 'description')