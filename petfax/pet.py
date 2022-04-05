from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
  return render_template('pets/index.html', pets=pets)

@bp.route('/<id>')
def show(id):
  return render_template('pets/show.html', pet=pets[int(id)-1])

