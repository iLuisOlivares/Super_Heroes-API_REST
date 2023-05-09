from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from ..models import Superhero
from ..models import Location
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class SuperheroView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0, name=""):
        if id != 0:
            superheroes = list(Superhero.objects.filter(id=id).values())
        elif name != "":
            superheroes = list(Superhero.objects.filter(
                name__icontains=name.lower().capitalize()).values())
        else:
            superheroes = list(Superhero.objects.values())

        if (len(superheroes) == 1):
            datos = {"message": "success",
                     "superhero": superheroes[0]
                     }
        elif len(superheroes) > 1:
            datos = {"message": "success",
                     "superheroes": superheroes
                     }
        else:
            datos = {"message": "No superheroes found"}

        return JsonResponse(datos, status=200)

    def post(self, request):

        body = json.loads(request.body)

        Superhero.objects.create(
            name=body['name'],
            alias=body['alias'],
            description=body['description'],
            publisher=body['publisher'],
            location_id=body['location_id'],
        )

        datos = {"message": "saved successfully",  "data": body}
        return JsonResponse(datos)

    def put(self, request, id):
        body = json.loads(request.body)
        superheroes = list(Superhero.objects.filter(id=id).values())
        if len(superheroes) > 0:
            location_instance = Location.objects.get(pk=body['location_id'])
            superHero = Superhero.objects.get(id=id)
            superHero.name = body['name']
            superHero.alias = body['alias']
            superHero.description = body['description']
            superHero.publisher = body['publisher']
            superHero.location_id = location_instance
            superHero.save()
            datos = {"message": "updated successfully", "data": body}
        else:
            datos = {"message": "No superhero found"}

        return JsonResponse(datos)

    def delete(self, request, id):
        superheroes = list(Superhero.objects.filter(id=id).values())
        if len(superheroes) > 0:
            Superhero.objects.get(id=id).delete()
            datos = {"message": "deleted successfully"}
        else:
            datos = {"message": "No superhero found"}
        return JsonResponse(datos)
