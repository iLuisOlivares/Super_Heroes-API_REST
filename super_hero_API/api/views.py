from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Superhero
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
