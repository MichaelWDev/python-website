from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
# Runs whenever you go to the main page.
def home():
	return render_template("home.html")