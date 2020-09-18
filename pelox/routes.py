from flask import render_template, url_for, flash, redirect
from pelox.forms import RegistrationForm, LoginForm
from pelox import app, bcrypt, db

@app.route("/")
@app.route("/landingpage/")
def landingpage ():
	return render_template('landingpage.html', title='landing page')

@app.route("/home/")
def home():
	return render_template('home.html', title='home')

@app.route("/registration/", methods=['POST', 'GET'])
def register ():
	form = RegistrationForm()
	import pdb; pdb.set_trace()

	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = Ordinaryuser( name=form.name.data, email= form.email.data, password= hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'registration successful, you are now able to log in')
		return redirect(url_for('login'))
	return render_template('register.html', title='register', form=form)

@app.route("/login/", methods=['POST', 'GET'])
def login():
	form = LoginForm()
	return render_template('login.html', title='login',  form=form)

@app.route("/account/")
def account():
	return render_template('account.html', title='account')