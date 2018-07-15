import json

class Recipe():
    def __init__(self):
        self.name = '' # String of the recipe name
        self.instructions = '' # HTML string
        self.ingredients = [] # Ingredients list of dicts (keys: name, qty, prepared)
        self.image_url = '' # URL pointing to the image file
        self.cuisine = '' # String of the cuisine
        self.likes = {'Dale': 'True', 'Jennifer': 'True', 'Parker': 'True', 'Isabelle': 'True'}

class ShoppingList():
    def __init__():
        self.name




spaghetti = Recipe()
spaghetti.name = 'Spaghetti'
spaghetti.instructions = '<ol><li>Boil noodles</li><li>Add sauce</li></ol>'
spaghetti.ingredients = [
    {'name':'spaghetti noodles', 'qty':'1 box', 'prepared':''},
    {'name':'spaghetti sauce', 'qty':'1 jar', 'prepared':''}
]
spaghetti.cuisine = 'Italian'

spaghetti_meatballs = Recipe()
spaghetti_meatballs.name = 'Spaghetti with Meatballs'
spaghetti_meatballs.instructions = '<ol><li>Boil noodles</li><li>Cook meatballs</li><li>Add sauce to meatballs</li><li>Add sauce and meatballs to noodles</li></ol>'
spaghetti_meatballs.ingredients = [
    {'name':'spaghetti noodles', 'qty':'1 box', 'prepared':''},
    {'name':'spaghetti sauce', 'qty':'1 jar', 'prepared':''},
    {'name':'meatballs', 'qty':'1 bag', 'prepared':''}
]
spaghetti_meatballs.cuisine = 'Italian'

