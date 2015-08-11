from flask import Flask
import configuration
from my_app.product.views import product_blueprint

app = Flask(__name__, template_folder='../templates')
app.config.from_object(configuration.DevelopmentConfig)
app.register_blueprint(product_blueprint)

