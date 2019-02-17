from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Role
from .. import db
import datetime

#views
@main.route('/')
def index():
    '''
    index veiw function
    '''
    title = 'My personal Blog'
    return render_template('index.html' , title = title)


@main.route('/user/<uname>')
def profile(uname):
    '''
    function that returns the profile page
    '''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)