from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Superhero
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


class SuperheroView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id != 0:
            superheroes = list(Superhero.objects.filter(id=id).values())

        else:
            superheroes = list(Superhero.objects.values())

        if len(superheroes) > 1:
            datos = {"message": "success",
                     "superheroes": superheroes
                     }
        elif (len(superheroes) == 1):
            datos = {"message": "success",
                     "superhero": superheroes[0]
                     }
        else:
            datos = {"message": "No superheroes found"}

        return JsonResponse(datos, status=200)

    def post(self, request):

        json_data = json.loads(request.body)
        Superhero.objects.create(
            name=json_data['name'],
            alter_ego=json_data['alter_ego'],
            description=json_data['description'])

        datos = {"message": "saved successfully",  "data": json_data}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        superheroes = list(Superhero.objects.filter(id=id).values())
        if len(superheroes) > 0:
            superHero = Superhero.objects.get(id=id)
            superHero.name = jd['name']
            superHero.alter_ego = jd['alter_ego']
            superHero.description = jd['description']
            superHero.save()
            datos = {"message": "updated successfully", "data": jd}
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
