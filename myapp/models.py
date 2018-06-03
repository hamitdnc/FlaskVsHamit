# external
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# internal
from myapp import db, login

# UserMixin ; User modeli ile current_user'i birbirine baglar
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password_hashed = db.Column(db.String(128), nullable=False, unique=True)

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


# class Tasks(db.Model):
#     """ Burayi hamit yapacak"""
#     pass
    
