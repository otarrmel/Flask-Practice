from flask import Flask
import configuration

app = Flask(__name__)
app.config.from_object(configuration.DevelopmentConfig)

from my_app.app_one import views
from my_app.app_one import models