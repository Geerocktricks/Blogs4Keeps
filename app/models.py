from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    '''
    user class to help create new users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship("Blog", backref= "user", lazy="dynamic")
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password) 


    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Blog(db.Model):
    """
    This is the class which we will use to create the blogs for the app
    """
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    category = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # comments = db.relationship("Comment", backref = "pitch", lazy = "dynamic")


    def save_blogs(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls,id):
        blog = Blog.query.filter_by(blog_id = blog.id).order_by(blog.time.desc())
        return reviews