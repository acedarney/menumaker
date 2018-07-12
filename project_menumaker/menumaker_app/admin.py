from django.contrib import admin
from .models import Recipe, Menu

class RecipeAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

class MenuAdmin(admin.ModelAdmin):
    autocomplete_fields = ['recipes']
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Menu, MenuAdmin)