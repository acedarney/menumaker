from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'flaskme'
}
db = MongoEngine(app)

class Recipe(db.Document):
    name = db.StringField()
    instructions = db.StringField()
    ingredients = db.ListField(db.StringField)

class Menu(db.Document):
    name = db.StringField()
    recipes = db.ListField(db.StringField)

@app.route('/')
def index():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)


# import mongoengine as me

# me.connect('menumaker-test')

# # Add data
# week1 = Menu(name='week1').save()
# week1.recipes = ['spaghetti', 'burgers']
# week1.save()
# spaghetti = Recipe(name='spaghetti', instructions='cook', ingredients=['noodles', 'spaghetti sauce', 'meatballs'])
# spaghetti.save()
# burgers = Recipe(name='burgers', instructions='grill', ingredients=['hamburgers', 'buns'])
# burgers.save()
# for recipe in Recipe.objects:
#     print(recipe.name)

# for menu in Menu.objects:
#     print(menu.name)