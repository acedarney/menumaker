import json

class Recipe():
    def __init__(self):
        self.name = '' # String of the recipe name
        self.instructions = '' # HTML string
        self.ingredients = [] # Ingredients list of dicts (keys: name, qty, prepared)
        self.image_url = '' # URL pointing to the image file
        self.cuisine = '' # String of the cuisine
        self.likes = {'Dale': 'True', 'Jennifer': 'True', 'Parker': 'True', 'Isabelle': 'True'}

    def __str__(self):
        return self.name

class ShoppingList():
    def __init__(self):
        self.name = ''
        self.shopping_list = {}

    def __str__(self):
        return self.name

    @staticmethod
    def add_contents(str1, str2):
        (qty1, item1) = str1.split(maxsplit=1)
        (qty2, item2) = str2.split(maxsplit=1)
        if item1 == item2:
            return ' '.join([str(int(qty1) + int(qty2)), item1])
        else:
            return ', '.join([str1, str2])

    def create_shopping_list(self, recipes_list):
        for recipe in recipes_list:
            for ingredient in recipe.ingredients:
                if ingredient['name'] in self.shopping_list:
                    self.shopping_list[ingredient['name']] = self.add_contents(self.shopping_list[ingredient['name']], ingredient['qty'])
                else:
                    self.shopping_list[ingredient['name']] = ingredient['qty']



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

shop_list = ShoppingList()
shop_list.name = 'Test Shopping List'

shop_list.create_shopping_list([spaghetti, spaghetti_meatballs])

print(spaghetti)
print(spaghetti_meatballs)
print(shop_list.shopping_list)