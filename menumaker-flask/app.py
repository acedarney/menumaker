from flask import Flask, render_template, url_for, redirect, jsonify, request
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from flask_marshmallow import Marshmallow
from marshmallow_mongoengine import ModelSchema

app = Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'menumaker_flask'}

db = MongoEngine(app)
ma = Marshmallow(app)
# db.init_app(app)

# Create models

class Ingredient(db.EmbeddedDocument):
    name = db.StringField()
    measure = db.StringField()
    qty = db.StringField()

class Recipe(db.Document):
    name = db.StringField()
    instructions = db.StringField()
    ingredients = db.ListField(db.EmbeddedDocumentField(Ingredient))
    # ingredients = db.StringField()

class Menu(db.Document):
    name = db.StringField()
    # recipes = db.ListField(db.StringField)

# Create serializers

class RecipeSchema(ModelSchema):
    class Meta:
        model = Recipe

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

# CRUD operations for API (Create, Read, Update, Delete)

@app.route('/api/recipes')
def get_recipes_api():
    all_recipes = Recipe.objects.all()
    result = recipes_schema.dump(all_recipes)
    return jsonify(result)
    
@app.route('/api/recipe/<id>')
def get_recipe_api(id):
    recipe = Recipe.objects.get_or_404(id=id)
    result = recipe_schema.dump(recipe)
    return jsonify(result)

@app.route('/api/add', methods=['POST'])
def add_recipe_api():
    new_data = request.get_json(force=True)
    new_recipe = recipe_schema.load(new_data)
    # for ingredient in new_recipe.ingredients:
    #     ingredient.data.save()
    new_recipe.data.save()
    result = recipe_schema.dump(new_recipe)
    return jsonify(new_recipe)
    
# Forms with WTForms

# RecipeForm = model_form(Recipe)





# Create Views (recipe list, recipe detail, menu list, menu detail)

@app.route('/')
def index():
    return 'Dale loves Jen'

@app.route('/recipes/clear')
def add():
    """
    Add a fixed document to the 'recipe' collection.  
    """
    Recipe.objects().delete()
    return redirect(url_for('view_recipes_list'))

@app.route('/recipes')
def view_recipes_list():
    """
    View all recipes
    """
    recipes = Recipe.objects.all()
    return render_template('recipe_list.html', recipes=recipes)

@app.route('/recipe/<name>')
def view_recipe_detail(name):
    """
    View a single recipe
    """
    recipe = Recipe.objects.get_or_404(name=name)
    return 'Recipe Name: {}'.format(recipe.name)

if __name__ == '__main__':
    app.run(debug=True) 