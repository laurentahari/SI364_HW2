from flask import Flask, request, render_template, redirect, url_for, flash, redirect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required

import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True

bootstrap = Bootstrap(app)
moment = Moment(app)

class AlbumEntryForm(FlaskForm):
    album = StringField('Enter the name of an album:', validators=[Required() ])
    chosen_option = RadioField('How much do you like this album? (1 low, 3 high)', choices=[('1', '1'), ('2', '2'), ('3', '3')], validators=[Required()])
    Submit = SubmitField('Submit') 

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/album_entry', methods = ['GET', 'POST'])
def album_entry():
    form = AlbumEntryForm ()
    return render_template('album_entry.html', form=form)


@app.route('/album_result', methods=['GET', 'POST'])
def album_result():
    form = AlbumEntryForm ()
    if form.validate_on_submit():
        album = form.album.data
        chosen_option = form.chosen_option.data
    return render_template('album_data.html', album=album, chosen_option=chosen_option)
    flash(form.errors)
    return redirect(url_for('album_entry'))

if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)


