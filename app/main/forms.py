from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    '''
    UpdateProfile class for bio updates
    '''
    bio = TextAreaField('Express your thoughts.',validators = [Required()])
    submit = SubmitField('Submit')
