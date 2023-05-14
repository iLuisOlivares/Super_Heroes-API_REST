from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from ..models import Supervillain
from ..models import Location
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Importar patron retry
from retrying import retry


class SupervillainView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    # Metodo get

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def get(self, request, id=0, name=""):
        if id != 0:
            supervillain = list(Supervillain.objects.filter(id=id).order_by('id').values())
        elif name != "":
            supervillain = list(Supervillain.objects.filter(
                name__icontains=name.lower().capitalize()).order_by('id').values())
        else:
            supervillain = list(Supervillain.objects.order_by('id').values())

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


    # Metodo post

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def post(self, request):

        body = json.loads(request.body)

        Supervillain.objects.create(
            name=body['name'],
            alias=body['alias'],
            description=body['description'],
            publisher=body['publisher'],
            nemesis=body['nemesis'],
            location_id=body['location_id'],
        )

        datos = {"message": "saved successfully",  "data": body}
        return JsonResponse(datos)

    # Metodo put

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def put(self, request, id):
        body = json.loads(request.body)
        supervillain = list(Supervillain.objects.filter(id=id).order_by('id').values())
        if len(supervillain) > 0:
            supervillain = Supervillain.objects.get(id=id)
            
            if 'name' in body:
                supervillain.name = body['name']

            if 'alias' in body:
                supervillain.alias = body['alias']

            if 'description' in body:
                supervillain.description = body['description']

            if 'publisher' in body:
                supervillain.publisher = body['publisher']

            if 'location_id' in body:
                location_instance = Location.objects.get(pk=body['location_id'])
                supervillain.location_id = location_instance
                
            supervillain.save()
            datos = {"message": "updated successfully", "data": body}
        else:
            datos = {"message": "No superhero found"}

        return JsonResponse(datos)

    # Metodo delete
    
    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def delete(self, request, id):
        supervillain = list(Supervillain.objects.filter(id=id).order_by('id').values())
        if len(supervillain) > 0:
            Supervillain.objects.get(id=id).delete()
            datos = {"message": "deleted successfully"}
        else:
            datos = {"message": "No superhero found"}
        return JsonResponse(datos)
