from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


#initializing the app
app = Flask(__name__)

#setting up configs
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views