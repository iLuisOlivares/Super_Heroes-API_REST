from rest_framework import serializers
from .models import Superhero, Supervillain, Location, Character


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'city', 'country', 'description')


class CharacterSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Character
        fields = ('superhero_name', 'name', 'alias', 'publisher',
                  'description', 'first_appearance','height', 'race', 'location', 'image')


class SuperheroSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Superhero
        fields = ('superhero_name', 'name', 'alias', 'publisher',
                  'description','first_appearance', 'height', 'race', 'location', 'image')


class SupervillainSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Supervillain
        fields = ('superhero_name', 'name', 'alias', 'publisher',
                  'description', 'first_appearance','height', 'race', 'location', 'image', 'nemesis')
