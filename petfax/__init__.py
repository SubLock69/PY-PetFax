from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'iuniuysad08hn34n87n183276ghn76hawer87h4uh4'

  @app.route('/')
  def hello():
    return 'Hello!'

  from . import (pet, facts)
  app.register_blueprint(pet.bp)
  app.register_blueprint(facts.bp)

  return app
