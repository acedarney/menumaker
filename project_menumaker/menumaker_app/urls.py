from django.urls import path, include
from rest_framework import routers
from .views import (RecipeListView, RecipeDetailView, MenuListView, MenuDetailView, MenuUpdateView, MenuAPIViewSet, RecipeAPIViewSet)

router = routers.DefaultRouter()
router.register('recipes', RecipeAPIViewSet)
router.register('menus', MenuAPIViewSet)

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list-view'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail-view'),
    path('menus', MenuListView.as_view(), name='menu-list-view'),
    path('menu/<int:pk>', MenuDetailView.as_view(), name='menu-detail-view'),
    path('menu/update/<int:pk>', MenuUpdateView.as_view(), name='menu-update-view'),
    path('api/', include(router.urls))
]