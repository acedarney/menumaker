from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, Menu

class RecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe
