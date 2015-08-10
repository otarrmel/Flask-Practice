from flask import Flask

app = Flask(__name__)
DEBUG = True

from my_app.raots import views
from my_app.raots import models