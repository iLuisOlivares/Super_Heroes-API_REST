from django.urls import path
from rest_framework import routers
from .viewsets import SuperheroViewSet, SupervillainViewSet, LocationViewSet, CharacterViewSet

from .vistas.CounterView import CounterView

router = routers.DefaultRouter()

router.register('api/characters', CharacterViewSet, 'characters')

router.register('api/superheroes', SuperheroViewSet, 'superh')

router.register('api/supervillains', SupervillainViewSet, 'superv')

router.register('api/locations', LocationViewSet, 'superl')

urlpatterns = router.urls + [

    path('api/counter', CounterView.as_view(), name='counter_list'),
]


# from .vistas.SuperheroView import SuperheroView
# from .vistas.LocationView import LocationView
# from .vistas.SupervillainView import SupervillainView

# urlpatterns = [

#     # Urls de Superhero
#     # Obtener todos los superheroes
#     path('superheroes/', SuperheroView.as_view(), name='superhero_list'),
#     #  GET, PUT DELETE | superhero por id
#     path('superheroes/<int:id>', SuperheroView.as_view(),name='superhero_process'),
#     #  Filtrar superheroes por nombre
#     path('superheroes/<name>', SuperheroView.as_view(),name='superhero_process'),

#     #  Urls de Supervillain
#     #  Obtener todos los supervillanos
#     path('supervillain/', SupervillainView.as_view(), name='supervillain_list'),
#     # GET, PUT DELETE | supervillano por id
#     path('supervillain/<int:id>', SupervillainView.as_view(),name='supervillain_process'),
#     #  Filtrar supervillanos por nombre
#     path('supervillain/<name>', SupervillainView.as_view(),name='supervillain_process'),

#     #  Urls de Location
#     #  Obtener todos los locations
#     path('locations/', LocationView.as_view(), name='location_list'),
#     # GET, PUT DELETE | location por id
#     path('locations/<int:id>', LocationView.as_view(), name='location_process'),
#     # Filtrar locations por nombre
#     path('locations/<name>', LocationView.as_view(), name='location_process'),
# ]
