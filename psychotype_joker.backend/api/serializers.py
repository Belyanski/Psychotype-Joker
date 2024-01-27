from rest_framework import serializers
from jokes.models import Category as JokeCategory, Joke
from storys.models import Category as StorysCategory, Storys

class JokeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JokeCategory
        fields = '__all__'

class JokeSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=JokeCategory.objects.all())

    class Meta:
        model = Joke
        fields = ['id', 'category', 'text']

class StorysCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StorysCategory
        fields = '__all__'

class StorysSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=StorysCategory.objects.all())

    class Meta:
        model = Storys
        fields = ['id', 'category', 'text']


