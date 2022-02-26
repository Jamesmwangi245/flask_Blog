from ensurepip import bootstrap
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initializing application
app=Flask(__name__)

#setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing Flask extension
bootstrap = Bootstrap(app)

from apps import news