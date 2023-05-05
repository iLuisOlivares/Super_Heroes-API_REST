from django.urls import path
from .views import SuperheroView

urlpatterns = [
    path('superheroes/', SuperheroView.as_view(), name='superhero_list'),
    path('superheroes/<int:id>', SuperheroView.as_view(),
         name='superhero_process'),
]
