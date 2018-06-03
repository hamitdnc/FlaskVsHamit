# external
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
# internal
from config_hamit import Config


app = Flask(__name__)
app.config.from_object(Config)

# Flask nesne referansını veritabanına vererek, db ile Flask app'i bağladık
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
# flask ile database'i baglar
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

from myapp import routes, models 






