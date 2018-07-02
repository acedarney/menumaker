from flask_mongoengine import MongoEngine

db = MongoEngine()

class Recipe(db.Document):
    name = db.StringField()
    instructions = db.StringField()
    ingredients = db.ListField(db.StringField)

class Menu(db.Document):
    name = db.StringField()
    recipes = db.ListField(db.StringField)