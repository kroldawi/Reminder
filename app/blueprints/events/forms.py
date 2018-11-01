from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AddEventForm(FlaskForm):
    name = StringField('What', validators = [DataRequired()])
    when = DateField('When', validators = [DataRequired()], format = '%Y-%m-%d')
    recurring = BooleanField('Recurring', default = 'checked')
    submit = SubmitField('Add')

class DeleteEventForm(FlaskForm):
    submit = SubmitField('Delete')
