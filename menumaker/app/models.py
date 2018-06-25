from djongo import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    # ingredients = models.ListField()