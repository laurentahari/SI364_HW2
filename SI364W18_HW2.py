## SI 364
## Winter 2018
## HW 2 - Part 1

## This homework has 3 parts, all of which should be completed inside this file (and a little bit inside the /templates directory).

## Add view functions and any other necessary code to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided are inside the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

import json
import requests
from flask import Flask, request, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'


####################
###### ROUTES ######
####################

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)


@app.route('/artistform')
def artistform():
	return render_template('artistform.html')

@app.route('/artistinfo')
def artistinfo():
	result = request.args
	specific_artist = result.get('artist')
	base_url = "https://itunes.apple.com/search?term=" 
	url = base_url + str(specific_artist)
	y = requests.get(url).text
	return render_template('artist_info.html', objects = json.loads(y)["results"])

@app.route('/artistlinks')
def artistlinks():
	return render_template("artist_links.html")

@app.route('/chosen/song/<artistName>')
def chosensong(artistName):
	base_url = "https://itunes.apple.com/search?term=" 
	url = base_url + str(artistName)
	y = requests.get(url).text
	return render_template("specific_artist.html", results = json.loads(y)["results"])


if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
