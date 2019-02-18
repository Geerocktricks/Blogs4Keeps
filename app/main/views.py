from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Role , Blog , Comment
from .forms import UpdateProfile,AddBlogForm,AddComment
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


@main.route("/<uname>/add/blog", methods = ["GET","POST"])
@login_required
def add_blog(uname):
    form = AddBlogForm()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    title = "Add a Blog Post"
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        category = form.category.data 
        dateOriginal = datetime.datetime.now()
        time = str(dateOriginal.time())
        time = time[0:5]
        date = str(dateOriginal)
        date = date[0:10]
        new_blog = Blog(title = title, content = blog, category = category,user = user, date = date,time = time)
        # new_blog.save_blog()  
        blogs = Blog.query.all()
        return redirect(url_for("main.categories" , category = category))
    return render_template("add_blog.html",form = form, title = title)

@main.route("/blogs/<category>")
def categories(category):
    blogs = None
    if category == "all":
        blogs = Blog.query.order_by(Blog.time.desc())
    else:
        Blogs = Blog.query.filter_by(category = category).all()

    return render_template("profile/profile.html", blogs = blogs, title = category.upper())