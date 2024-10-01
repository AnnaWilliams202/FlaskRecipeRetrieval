from flask import Flask
import json

recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'], 'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'], 'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'], 'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}

file_name = 'recipes.json' #convert variable in json file

with open(file_name, 'w') as f: # open file in write mode
    json.dump(recipes, f, indent=4)

print(f'Dictionary converted to json succesfully. file name = {file_name}')

app = Flask(__name__)

with open('recipes.json', 'r') as f:
    recipes = json.load(f)


@app.route('/recipes/<recipe_id>')
def get_recipe(recipe_id):
    recipe = recipes[recipe_id]
    if recipe:
        return recipe
    else:
        return {'message': 'Recipe not found'}, 404


@app.route('/')
def index():
    return 'Homepage'

app.run(debug=True)


