from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from ..models import Location
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Patron retry
from retrying import retry


class LocationView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def get(self, request, id=0, name=""):
        if id != 0:
            locations = list(Location.objects.filter(id=id).values())
        elif name != "":
            locations = list(Location.objects.filter(
                city__icontains=name.lower().capitalize()).values())
        else:
            locations = list(Location.objects.values())
        if (len(locations) == 1):
            datos = {"message": "success",
                     "location": locations[0]
                     }

        elif len(locations) > 1:
            datos = {"message": "success",
                     "locations": locations
                     }
        else:
            datos = {"message": "No locations found"}

        return JsonResponse(datos, status=200)

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def post(self, request):

        json_data = json.loads(request.body)
        Location.objects.create(
            city=json_data['city'],
            country=json_data['country'],
            description=json_data['description'])

        datos = {"message": "saved successfully",  "data": json_data}
        return JsonResponse(datos)

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def put(self, request, id):
        jd = json.loads(request.body)
        location = list(Location.objects.filter(id=id).values())
        if len(location) > 0:
            location = Location.objects.get(id=id)
            location.name = jd['name']
            location.city = jd['city']
            location.country = jd['country']
            location.save()
            datos = {"message": "updated successfully", "data": jd}
        else:
            datos = {"message": "No location found"}

        return JsonResponse(datos)

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def delete(self, request, id):
        locations = list(Location.objects.filter(id=id).values())
        if len(locations) > 0:
            Location.objects.get(id=id).delete()
            datos = {"message": "deleted successfully"}
        else:
            datos = {"message": "No location found"}
        return JsonResponse(datos)
