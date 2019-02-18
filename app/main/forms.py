from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    '''
    UpdateProfile class for bio updates
    '''
    bio = TextAreaField('Express your thoughts.',validators = [Required()])
    submit = SubmitField('Submit')

class AddBlogForm(FlaskForm):
    title = StringField("Title", validators = [Required()])
    blog = TextAreaField("Add a blog", validators = [Required()])
    category = StringField('Categories')
    submit = SubmitField("Add blog")

class AddComment(FlaskForm):
    content = TextAreaField("Add comment")
    submit = SubmitField("Add")