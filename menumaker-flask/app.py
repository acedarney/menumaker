from flask import Flask, render_template, url_for, redirect
from flask_mongoengine import MongoEngine
# from models import db, Recipe, Menu

app = Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'menumaker_flask'}


db = MongoEngine()
db.init_app(app)

class Recipe(db.Document):
    name = db.StringField()
    instructions = db.StringField()
    # ingredients = db.ListField(db.StringField)
    ingredients = db.StringField()

class Menu(db.Document):
    name = db.StringField()
    # recipes = db.ListField(db.StringField)



@app.route('/')
def index():
    return 'Dale loves Jen'

@app.route('/add')
def add():
    """
    Add a fixed document to the 'recipe' collection.  
    """
    Recipe.objects().delete()
    Recipe(name='Spaghetti', 
           instructions='Cook noodles. Add sauce.', 
           ingredients='Noodles').save()
    
    return redirect(url_for('view_recipes_list'))

@app.route('/recipes')
def view_recipes_list():
    """
    View all recipes
    """
    recipes = Recipe.objects.all()
    return render_template('recipe_list.html', recipes=recipes)

@app.route('/recipe/<name>')
def view_single_recipe(name):
    """
    View a single recipe
    """
    recipe = Recipe.objects.get_or_404(name=name)
    return 'Recipe Name: {}'.format(recipe.name)

if __name__ == '__main__':
    app.run(debug=True) 