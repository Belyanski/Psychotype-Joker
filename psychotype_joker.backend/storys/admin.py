from django.contrib import admin
from .models import Category, Storys


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Storys)
class JokeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'text')
