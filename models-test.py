import mongoengine as me

me.connect('menumaker-test')

class Recipe(me.Document):
    name = me.StringField()
    instructions = me.StringField()
    ingredients = me.ListField(me.StringField)

class Menu(me.Document):
    name = me.StringField()
    recipes = me.ListField(me.StringField)

# Add data
week1 = Menu(name='week1').save()
spaghetti = Recipe(name='spaghetti', instructions='cook', ingredients=['noodles', 'spaghetti sauce', 'meatballs']).save()
burgers = Recipe(name='burgers', instructions='grill', ingredients=['hamburgers', 'buns']).save()
week1.recipes = ['spaghetti', 'burgers']
week1.save()

for recipe in Recipe.objects:
    print(recipe.name)

for menu in Menu.objects:
    print(menu.name)