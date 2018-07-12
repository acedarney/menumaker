from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Recipe, Menu
from django.urls import reverse_lazy

class RecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'

class MenuListView(ListView):
    model = Menu

class MenuDetailView(DetailView):
    model = Menu

class MenuCreate(CreateView):
    model = Menu
    fields = '__all__'

class MenuUpdateView(UpdateView):
    model = Menu
    fields = ['recipes']
    template_name_suffix = '_update_form'
