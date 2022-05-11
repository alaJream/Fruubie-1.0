# Create your forms here.from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, TextAreaField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from app.models import User, Post

class PostForm(FlaskForm):
  """Form for adding/updating a GroceryStore"""
  name = StringField('Name of Produce', validators=[DataRequired()])
  address = StringField('Address for Pickup')

def get_posts():
  return Post.query

class CommentForm(FlaskForm):
  """Form for adding a comment"""
  comment = TextAreaField('Comment', validators=[DataRequired()])