from flask import Flask
from flask_pymongo import PyMongo
import jsonify

app = Flask(__name__)
mongo = PyMongo(app)

app.config['MONGO_DBNAME'] = 'menumaker_flask'
# app.config['MONGO_URI'] = 'mongodb+srv://acedarney:E46&YUg#pYkG@menumaker-oyxdx.mongodb.net/test?retryWrites=true'

@app.route('/')
def index():
    return 'Dale loves Jen'

@app.route('/add')
def add():
    """
    Add a fixed document to the 'recipes' collection.  
    TODO: update to a form that adds the proper fields
    """
    recipes = mongo.db.recipes
    recipes.insert({'name' : 'Spaghetti',
                    'instructions' : 'Cook noodles.  Add sauce.',
                    'ingredients' : [
                        {'name' : 'Noodles'},
                        {'name' : 'Sauce'}]
                    })
    return 'Recipe added.'

@app.route('/recipe/<name>')
def view_single_recipe(name):
    """
    Retrieve a recipe name and instructions as text.
    TODO: update to return JSON of the full document (with nested list of ingredients)
    """
    recipes = mongo.db.recipes
    requested_recipe = recipes.find_one({'name' : name})

    result = {'name' : requested_recipe['name'],
              'instructions' : requested_recipe['instructions']
             }

    return ' '.join([requested_recipe['name'], requested_recipe['instructions']])


if __name__ == '__main__':
    app.run(debug=True) 