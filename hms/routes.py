from flask import render_template,flash,url_for,redirect,request
from hms.forms import RegistrationForm,LoginForm
from hms.models import User,Post
from hms import app
@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/Registration')
def Registration():
	form=RegistrationForm()
    return render_template('Registration.html')

@app.route('/Update')
def update():
    return render_template('Update.html')

@app.route('/Delete')
def delete():
    return render_template('Delete.html')

@app.route('/Viewall')
def viewall():
    return render_template('Viewall.html')

@app.route('/View')
def view():
    return render_template('View.html')


@app.route('/Pharmacy')
def pharmacy():
    return render_template('Pharmacy.html')


@app.route('/Diagnostics')
def diagnostics():
    return render_template('Diagnostics.html')
