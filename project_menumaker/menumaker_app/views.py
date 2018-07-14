from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Recipe, Menu
from .serializers import MenuSerializer, RecipeSerializer

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

class MenuAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Menus to be viewed or edited.CreateView
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class RecipeAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recipes to be viewed or edited.CreateView
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
