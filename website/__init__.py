# Turns website folder into a package, allows importing.
from flask import Flask

def create_app():
    app = Flask(__name__) # Represents the name of the file.
    app.config['SECRET_KEY'] = ''

    return app

    # TIME: 10:36