from flask import Flask
from flask_migrate import Migrate

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'iuniuysad08hn34n87n183276ghn76hawer87h4uh4'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:codeking420@localhost:5432/petfax'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  from . import models
  models.db.init_app(app)
  migrate = Migrate(app, models.db)

  @app.route('/')
  def hello():
    return 'Hello!'

  from . import (pet, facts)
  app.register_blueprint(pet.bp)
  app.register_blueprint(facts.bp)

  return app
