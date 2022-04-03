from flask import (Blueprint, render_template)

bp = Blueprint('facts', __name__, url_prefix='/facts')

#Show all facts
@bp.route('/')
def index():
  return 'List of Facts'

#Show new fact form
@bp.route('/new')
def showForm():
  return render_template('newFactForm.html')

#POST route for adding fact
@bp.route('/new', methods='POST')
def addFact():
  return 'Fact Added (But not really lol)'