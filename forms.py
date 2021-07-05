from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField
from wtforms.validators import DataRequired


class ExpensesForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description')
    cathegory = StringField('cathegory', validators=[DataRequired()])
    amount = FloatField('amount', validators=[DataRequired()])
    month = IntegerField('month', validators=[DataRequired()])
