from app import myobj
from flask import render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class cityForm(FlaskForm):
    city = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@myobj.route("/", methods=('GET', 'POST'))

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

def home():
    form = cityForm()
    if form.validate_on_submit ():
        flash("{}" .format(form.city.data))
        #return render_template('home.html', name=name, city_names=city_names, form=form)
    return render_template('home.html', name=name, city_names=city_names, form=form)