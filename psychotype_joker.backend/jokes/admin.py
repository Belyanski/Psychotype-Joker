from django.contrib import admin
from .models import Category, Joke


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'text')

