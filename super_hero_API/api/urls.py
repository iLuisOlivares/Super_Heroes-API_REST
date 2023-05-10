from django.urls import path
from .vistas.SuperheroView import SuperheroView
from .vistas.LocationView import LocationView
from .vistas.SupervillainView import SupervillainView

urlpatterns = [
    path('superheroes/', SuperheroView.as_view(), name='superhero_list'),
    path('superheroes/<int:id>', SuperheroView.as_view(),
         name='superhero_process'),
    path('superheroes/<name>', SuperheroView.as_view(),
         name='superhero_process'),
    path('supervillain/', SupervillainView.as_view(), name='supervillain_list'),
    path('supervillain/<int:id>', SupervillainView.as_view(),
         name='supervillain_process'),
    path('supervillain/<name>', SupervillainView.as_view(),
         name='supervillain_process'),
    path('locations/', LocationView.as_view(), name='location_list'),
    path('locations/<int:id>', LocationView.as_view(), name='location_process'),
    path('locations/<name>', LocationView.as_view(), name='location_process'),
]
