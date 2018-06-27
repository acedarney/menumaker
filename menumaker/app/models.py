from djongo import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    units = models.CharField(max_length=10)
    amount = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    ingredients = models.ArrayModelField(model_container=Ingredient)
    # tags = models.ArrayModelField(model_container=Tag, null=True)

    def __str__(self):
        return self.name


