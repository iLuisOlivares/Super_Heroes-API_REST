from django.urls import path
from rest_framework import routers
from .vistas.SuperheroView import SuperheroView
from .vistas.LocationView import LocationView
from .vistas.SupervillainView import SupervillainView

router = routers.DefaultRouter()

# router.register('superheroes', SuperheroView, 'api')
# router.register('superheroes/<int>:id', SuperheroView, 'api')
# router.register('superheroes/<name>', SuperheroView, 'api')

# router.register('supervillain', SupervillainView, 'api')
# router.register('supervillain/<int>:id', SupervillainView, 'api')
# router.register('supervillain/<name>', SupervillainView, 'api')

# router.register('locations', LocationView, 'api')
# router.register('locations/<int>:id', LocationView, 'api')
# router.register('locations/<name>', LocationView, 'api')

# urlPatterns = router.urls

urlpatterns = [
    
    # Urls de Superhero
    # Obtener todos los superheroes
    path('superheroes/', SuperheroView.as_view(), name='superhero_list'),
     # GET, PUT DELETE | superhero por id
    path('superheroes/<int:id>', SuperheroView.as_view(),name='superhero_process'),
     # Filtrar superheroes por nombre
    path('superheroes/<name>', SuperheroView.as_view(),name='superhero_process'),

     # Urls de Supervillain
     # Obtener todos los supervillanos
    path('supervillain/', SupervillainView.as_view(), name='supervillain_list'),
    # GET, PUT DELETE | supervillano por id
    path('supervillain/<int:id>', SupervillainView.as_view(),name='supervillain_process'),
     # Filtrar supervillanos por nombre
    path('supervillain/<name>', SupervillainView.as_view(),name='supervillain_process'),

     # Urls de Location
     # Obtener todos los locations
    path('locations/', LocationView.as_view(), name='location_list'),
    # GET, PUT DELETE | location por id
    path('locations/<int:id>', LocationView.as_view(), name='location_process'),
    # Filtrar locations por nombre
    path('locations/<name>', LocationView.as_view(), name='location_process'),
]