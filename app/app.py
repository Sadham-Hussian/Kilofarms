import os

from flask import Flask
from flask_cors import CORS
from . import settings, controllers, models
from .extensions import db

project_dir = os.path.dirname(os.path.abspath(__file__))

def create_app(config_object=settings):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(config_object)

	register_extensions(app)
	register_blueprints(app)
	return app

def register_extensions(app):
	""" Register Flask extensions."""
	db.init_app(app)

	with app.app_context():
		db.create_all()
	return None

def register_blueprints(app):
	"""Register Flask blueprints."""
	app.register_blueprint(controllers.auth.blueprint)
	app.register_blueprint(controllers.products.blueprint)
	app.register_blueprint(controllers.home.blueprint)
	app.register_blueprint(controllers.web.blueprint)

	return None

app = create_app()
CORS(app)