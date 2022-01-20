# Turns website folder into a package, allows importing.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Database
from os import path
from flask_login import LoginManager, login_manager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
	app = Flask(__name__) # Represents the name of the file.
	app.config['SECRET_KEY'] = 'GLHMNK7979'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Database is located in DB_NAME.
	db.init_app(app) # Assigns database to the app.

	# Blueprints
	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix = '/')
	app.register_blueprint(auth, url_prefix = '/')

	from .models import User, Note

	create_database(app)

	# Tells Flask how to load a user.
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	return app

def create_database(app):
	if not path.exists('website/' + DB_NAME):
		db.create_all(app = app)
		print('Created Database!')