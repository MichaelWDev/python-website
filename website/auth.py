from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
	data = request.form
	print(data)
	return render_template("login.html", boolean = True)

@auth.route('/logout')
def logout():
	return "<p>Test</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
		print("Test!")
		email      = request.form.get('email')
		first_name = request.form.get('firstName')
		password1  = request.form.get('password1')
		password2  = request.form.get('password2')

		if len(email) < 4:
			flash('Email must be greater than 3 characters.', category='error') # Flashes text on screen.
		elif len(first_name) < 2:
			flash('First name must be greater than 1 character.', category='error')
		elif password1 != password2:
			flash('Passwords do not match.', category='error')
		elif len(password1) < 7:
			flash('Password must be at least 7 character.', category='error')
		else:
			# Add user to database.
			flash('Account created!', category='success')

	return render_template("signup.html")