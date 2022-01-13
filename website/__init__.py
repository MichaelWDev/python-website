# Turns website folder into a package, allows importing.
from flask import Flask

def create_app():
    app = Flask(__name__) # Represents the name of the file.
    app.config['SECRET_KEY'] = ''

    # Blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app