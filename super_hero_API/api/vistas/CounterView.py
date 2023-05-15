from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from ..models import Supervillain
from ..models import Superhero
from ..models import Location
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Importar patron retry
from retrying import retry


class CounterView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    # Saber la cantidad de entidades en la base de datos
    @retry(stop_max_attempt_number=5, wait_fixed=1000)
    def get(self, request, id=0, name=""):
        print("\nVerificando el patron retry")

        supervillain = list(Supervillain.objects.order_by('id').values())
        superhero = list(Superhero.objects.order_by('id').values())
        locations = list(Location.objects.order_by('id').values())


        datos = {
                "message": "succes",
                 "supervillain_count": len(supervillain),
                 "superhero_count": len(superhero),
                 "location_count": len(locations),
                 }

        return JsonResponse(datos, status=200)
