from rest_framework import serializers
from .models import Menu, Recipe


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'url', 'name', 'recipes')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'url', 'name', 'image', 'instructions', 'ingredients', 'cuisine', 'likes')