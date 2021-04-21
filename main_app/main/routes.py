#   importing basic flask module
from flask import render_template
from flask import Blueprint

#   initializing blueprint
main = Blueprint('main', __name__)

#   default route
@main.route('/')
def index():
    return render_tempate('index.html')

#   about route
@main.route('/about')
def about():
    return render_temmplate('about.html', title='About Us')