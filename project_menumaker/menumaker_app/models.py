from django.db import models
from django.contrib.postgres.fields import HStoreField, ArrayField
from ckeditor.fields import RichTextField
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField(max_length=50, default='Name')
    image = models.URLField(max_length=300, default='https://pixabay.com/photo-575434/')
    instructions = RichTextField(default='')
    # ingredients = ArrayField(HStore(), default=[{'name':'', 'qty':''}])
    ingredients = ArrayField(models.CharField(max_length=100, default='Ingredient', null=True), default=['Ingredient'])
    cuisine = models.CharField(max_length=30, default='Cuisine')
    likes = HStoreField(default={"Dale": "False", "Jennifer": "False", "Isabelle": "False", "Parker": "False"})

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})

class Menu(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu-detail', kwargs={'pk': self.pk})