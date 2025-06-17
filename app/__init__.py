

import os
from flask import Flask

from .models import db


def create_app():
 
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'finance.db')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'qualquer-string-aleatoria-e-secreta'

    db.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app