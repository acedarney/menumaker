from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import AddRecipeToCurrentMenu
from .models import Recipe, Menu

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

# Perhaps this could just be a FormView?
def add_recipe_to_menu(request, pk):
    if request.method == 'POST':
        form = AddRecipeToCurrentMenu(request.POST)
        if form.is_valid():
            recipe_to_add = Recipe.objects.get(name=form.recipe_name)
            current_menu = Menu.objects.get(id=pk)
            current_menu.recipes.add(recipe_to_add)            
            return HttpResponseRedirect('/menus/')
    else:
        form = AddRecipeToCurrentMenu()
    return render(request, 'add_recipe_to_menu.html', {'form': form}) #TODO: this can't find the template