from flask import render_template
# from app import app
from . import main
from flask_login import login_required

#views
@main.route('/')
def index():
    '''
    index veiw function
    '''
    title = 'My personal Blog'
    return render_template('index.html' , title = title)