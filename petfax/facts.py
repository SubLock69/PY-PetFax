from flask import (Blueprint, redirect, render_template, request)
from . import models

bp = Blueprint('fact', __name__, url_prefix='/facts')

#Accept new fact
@bp.route('/', methods=('GET','POST'))
def factIndex():
  if request.method == 'POST':
    submitter = request.form['submitter']
    fact = request.form['fact']

    new_fact = models.Fact(submitter=submitter,fact=fact)
    models.db.session.add(new_fact)
    models.db.session.commit()
    return redirect('/facts')

  return render_template('facts/index.html', facts=[])

#Show new fact form
@bp.route('/new')
def showForm():
  return render_template('facts/new.html')