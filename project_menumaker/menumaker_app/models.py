from django.db import models
from django.contrib.postgres.fields import HStoreField

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    instructions = models.TextField()
    ingredients = HStoreField()
    cuisine = models.CharField(max_length=30)
    likes = HStoreField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    recipes = models.ManyToManyField(Recipe)