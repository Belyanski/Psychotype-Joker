from random import choice

from rest_framework import viewsets, status
from rest_framework.response import Response
from jokes.models import Category as JokeCategory, Joke
from storys.models import Category as StorysCategory, Storys
from .serializers import JokeCategorySerializer, JokeSerializer, StorysCategorySerializer, StorysSerializer

from rest_framework.decorators import action

class JokeViewSet(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def categories(self, request, *args, **kwargs):
        categories = JokeCategory.objects.all()
        serializer = JokeCategorySerializer(categories, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], name='random_joke')
    def random_joke(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            random_joke = choice(queryset)
            serializer = self.get_serializer(random_joke)
            return Response(serializer.data)
        else:
            return Response({"detail": "No jokes available."}, status=status.HTTP_404_NOT_FOUND)


class StorysViewSet(viewsets.ModelViewSet):
    queryset = Storys.objects.all()
    serializer_class = StorysSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def categories(self, request, *args, **kwargs):
        categories = StorysCategory.objects.all()
        serializer = StorysCategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], name='random_story')
    def random_story(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            random_story = choice(queryset)
            serializer = self.get_serializer(random_story)
            return Response(serializer.data)
        else:
            return Response({"detail": "No stories available."}, status=status.HTTP_404_NOT_FOUND)