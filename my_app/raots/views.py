from my_app import app
from my_app.raots.models import MESSAGE


@app.route('/')
@app.route('/index')
def hello_world():
    return MESSAGE['default']