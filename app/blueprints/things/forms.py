from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired


class FormFieldFactory():
    def create_add_thing_form(self, tags):
        form = AddThingForm()
        form.tags.choices = tags

        return form
        

class AddThingForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    submit = SubmitField('Add')
    tags = SelectMultipleField('Tags', choices = [])


class DeleteThingForm(FlaskForm):
    submit = SubmitField('Delete')