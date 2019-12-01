from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')
    
class BlogForm(FlaskForm):
    title = StringField('Blog Title')
    topic = StringField('Topic')
    blog = TextAreaField('Blog Content') 
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')


