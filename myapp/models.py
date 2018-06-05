# external
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
# internal
from myapp import db, login

# UserMixin ; User modeli ile current_user'i birbirine baglar


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password_hashed = db.Column(db.String(128), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    def set_password(self, password):
        """ parolayi kriptolar"""
        self.password_hashed = generate_password_hash(password)

    def check_password(self, password):
        """kriptolu parolayi kontrol eder, boolean deger doner. """
        return check_password_hash(self.password_hashed, password)

    def __repr__(self):
        return "<User %r>" % self.username


# kullanici session'ı tutmasi icin
@login.user_loader
def load_user(id):
    return User.query.get(id)


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(280), nullable=False)
    released_date = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

    def __repr__(self):
        return "<Task %r>" % self.name

    def get_reported_name(self):
        return User.query.get(self.user_id).username



class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))