from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import FileField
from wtforms.validators import DataRequired


class AlbumForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    by = StringField('by', validators=[DataRequired()])
    year = StringField('year', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
