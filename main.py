from website import create_app

app = create_app()

if __name__ == '__main__': # Runs the web server off of main.py only.
	app.run(debug = True) # Any changes to python code re-runs the website.