# external
from flask import render_template
# internal
from myapp import app
from myapp.forms import LoginForm




@app.route('/')
@app.route('/home')
def home():
	myval = {
		'username' : "Hamit",
		'password' : "Çok gizli"
	}
	return render_template('index.html', title="Anasayfa", bilgi=myval )


@app.route('/profile')
def profile():
	
	posts = [
		{'title':'Başlık 1', 'content':'Bu yazı ben tarafından yazıldı!'},
		{'title':'Başlık 2', 'content':'Bu yazı sen tarafından yazıldı!'},
		{'title':'Başlık 3', 'content':'Bu yazı o tarafından yazıldı!'},
		{'title':'Başlık 4', 'content':'Bu yazı biz tarafından yazıldı!'},
	]

	return render_template('profile.html', title='Profil Sayfası',posts=posts)


@app.route('/login')
def login():
	form = LoginForm()

	return render_template('login.html', title="Login Sayfam", form=form)