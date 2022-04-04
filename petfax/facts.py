from flask import (Blueprint, redirect, render_template, request)

bp = Blueprint('fact', __name__, url_prefix='/facts')

#Accept new fact
@bp.route('/', methods=('GET','POST'))
def factIndex():
  if request.method == 'POST':
    print(request.form)
    return redirect('/facts')

  return 'Facts Index'

#Show new fact form
@bp.route('/new')
def showForm():
  return render_template('newFactForm.html')