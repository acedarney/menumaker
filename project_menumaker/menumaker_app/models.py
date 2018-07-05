from django.db import models
from django.contrib.postgres.fields import HStoreField, ArrayField

class Recipe(models.Model):
    name = models.CharField(max_length=50, default='Name')
    instructions = models.TextField(default='Instructions')
    ingredients = ArrayField(models.CharField(max_length=100, default='Ingredient', null=True), default=['Ingredient'])
    cuisine = models.CharField(max_length=30, default='Cuisine')
    likes = HStoreField(default={"Dale": "True"})

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    recipes = models.ManyToManyField(Recipe)