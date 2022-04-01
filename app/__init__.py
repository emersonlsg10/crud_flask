import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/youtube'

    db = SQLAlchemy(app)
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # apply the blueprints to the app
    from app.usuario.views import usuario_bp

    app.register_blueprint(usuario_bp, url_prefix="/usuarios")

    app.add_url_rule("/", endpoint="index")

    return app
