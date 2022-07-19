from flask import Flask
from config import Config


app = Flask(__name__, static_folder='View/static',template_folder='View/templates')
app.config.from_object(Config)

from application.View import routes