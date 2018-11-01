from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTagForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    submit = SubmitField('Add')


class DeleteTagForm(FlaskForm):
    submit = SubmitField('Delete')