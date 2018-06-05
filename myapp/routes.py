# external
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user
# sisteme giris yapan kullaniciyi temsil eder.
from flask_login import current_user
# internal
from myapp import app
from myapp.forms import LoginForm, RegisterForm, TaskForm
from myapp.models import User, Task
from myapp import db


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = TaskForm()
    # veritabanından select * from sorgusu gibi butun gorevleri aldik
    tasks = Task.query.all()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        task = Task(name=name, description=description)
        # task'in user_id'sine mevcut kullanicinin id'sini atadik.
        task.user_id = current_user.id
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('index.html', title="Anasayfa", form=form, tasks=tasks)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # formdan gelen username veritabanında var mi
        user = User.query.filter_by(username=username).first()
        # kullanici None degilse VE parola dogru ise
        if user is not None and user.check_password(password):
            flash("Giriş başarılı")
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Kullanıcı adı veya parola hatali")
            return redirect(url_for('login'))
    return render_template('login.html', title="Login Sayfam", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    is_admin=True)

        user.set_password(form.password.data)
        # veritabanına kayıt için session'a kullanıcıyı ekle
        db.session.add(user)
        # veritabanına gönder
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', title="Kaydol", form=form)


@app.route('/profile')
def profile():

    return render_template('profile.html', title='Profil Sayfası')
