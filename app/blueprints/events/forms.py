from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired


class FormFieldFactory():
    def create_add_event_form(self, tags):
        form = AddEventForm()
        form.tags.choices = tags

        return form

class AddEventForm(FlaskForm):
    name = StringField('What', validators = [DataRequired()])
    when = DateField('When', validators = [DataRequired()], format = '%Y-%m-%d')
    recurring = BooleanField('Recurring', default = 'checked')
    tags = SelectMultipleField('Tags', choices = [])
    submit = SubmitField('Add')

class DeleteEventForm(FlaskForm):
    submit = SubmitField('Delete')
