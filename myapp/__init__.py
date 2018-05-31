# external
from flask import Flask

# internal
from config_hamit import Config


app = Flask(__name__)
app.config.from_object(Config)



from myapp import routes 






