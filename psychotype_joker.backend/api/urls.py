from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import JokeViewSet, StorysViewSet

router_v1 = DefaultRouter()
router_v1.register(r'jokes', JokeViewSet, basename='jokes')
router_v1.register(r'storys', StorysViewSet, basename='storys')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('jokes/random_joke/', JokeViewSet.as_view({'get': 'random_joke'}), name='random-joke'),
    path('storys/random_story/', StorysViewSet.as_view({'get': 'random_story'}), name='random-story'),
]
