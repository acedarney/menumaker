from django.urls import path, include
from rest_framework import routers
from .views import (RecipeListView, RecipeDetailView, MenuListView, MenuDetailView, MenuUpdateView, MenuAPIViewSet, RecipeAPIViewSet)

router = routers.DefaultRouter()
router.register('recipes', RecipeAPIViewSet)
router.register('menus', MenuAPIViewSet)

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('menus', MenuListView.as_view(), name='menu-list'),
    path('menu/<int:pk>', MenuDetailView.as_view(), name='menu-detail'),
    path('menu/update/<int:pk>', MenuUpdateView.as_view(), name='menu-update'),
    path('api/', include(router.urls), name='rest-framework')
]