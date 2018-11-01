from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddThingForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    submit = SubmitField('Add')


class DeleteThingForm(FlaskForm):
    submit = SubmitField('Delete')