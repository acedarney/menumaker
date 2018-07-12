from django.urls import path
from .views import RecipeListView, RecipeDetailView, MenuListView, MenuDetailView, MenuUpdateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('menus', MenuListView.as_view(), name='menu-list'),
    path('menu/<int:pk>', MenuDetailView.as_view(), name='menu-detail'),
    path('menu/<int:pk>/update', MenuUpdateView.as_view(), name='menu-update')
]