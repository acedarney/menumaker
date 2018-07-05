from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail')
]