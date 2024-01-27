from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import JokeViewSet, StorysViewSet

router_v1 = DefaultRouter()
#router_v1.register(r'users', CustomUserViewSet, basename='users')
#router_v1.register(r'tags', TagViewSet, basename='tags')
router_v1.register(r'storys', StorysViewSet, basename='storys')
router_v1.register(r'jokes', JokeViewSet, basename='jokes')


urlpatterns = [
    path('', include(router_v1.urls)),
    #path('', include('djoser.urls')),
    #path('auth/', include('djoser.urls.authtoken')),
]
