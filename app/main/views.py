from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Role
from .forms import UpdateProfile
from .. import db,photos
import datetime
import markdown2  

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
    title = 'My personal Blog'

    return render_template("profile/profile.html", user = user , title = title)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/blog/<int:id>')
def single_blog(id):
    blog=Blog.query.get(id)
    if blog is None:
        abort(404)
    format_blog = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('blog.html',blog = blog,format_blog=format_blog)