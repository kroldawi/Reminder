from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired


class FormFieldFactory():
    def create_add_document_form(self, tags):
        form = AddDocumentForm()
        form.tags.choices = tags

        return form
        
        
class AddDocumentForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    value = StringField('Value')
    tags = SelectMultipleField('Tags', choices = [])
    submit = SubmitField('Add')


class DeleteDocumentForm(FlaskForm):
    submit = SubmitField('Delete')