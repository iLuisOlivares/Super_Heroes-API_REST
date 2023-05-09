from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from ..models import SuperVillain
from ..models import Location
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class SupervillainView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0, name=""):
        if id != 0:
            supervillain = list(SuperVillain.objects.filter(id=id).values())
        elif name != "":
            supervillain = list(SuperVillain.objects.filter(
                name__icontains=name.lower().capitalize()).values())
        else:
            supervillain = list(SuperVillain.objects.values())

        if (len(supervillain) == 1):
            datos = {"message": "success",
                     "superhero": supervillain[0]
                     }
        elif len(supervillain) > 1:
            datos = {"message": "success",
                     "supervillain": supervillain
                     }
        else:
            datos = {"message": "No supervillain found"}

        return JsonResponse(datos, status=200)

    def post(self, request):

        body = json.loads(request.body)

        SuperVillain.objects.create(
            name=body['name'],
            alias=body['alias'],
            description=body['description'],
            publisher=body['publisher'],
            nemesis=body['nemesis'],
            location_id=body['location_id'],
        )

        datos = {"message": "saved successfully",  "data": body}
        return JsonResponse(datos)

    def put(self, request, id):
        body = json.loads(request.body)
        supervillain = list(SuperVillain.objects.filter(id=id).values())
        if len(supervillain) > 0:
            location_instance = Location.objects.get(pk=body['location_id'])
            supervillain = SuperVillain.objects.get(id=id)
            supervillain.name = body['name']
            supervillain.alias = body['alias']
            supervillain.description = body['description']
            supervillain.publisher = body['publisher']
            supervillain.nemesis = body['nemesis']
            supervillain.location_id = location_instance
            supervillain.save()
            datos = {"message": "updated successfully", "data": body}
        else:
            datos = {"message": "No superhero found"}

        return JsonResponse(datos)

    def delete(self, request, id):
        supervillain = list(SuperVillain.objects.filter(id=id).values())
        if len(supervillain) > 0:
            SuperVillain.objects.get(id=id).delete()
            datos = {"message": "deleted successfully"}
        else:
            datos = {"message": "No superhero found"}
        return JsonResponse(datos)
