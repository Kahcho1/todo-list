from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    desc = StringField("Add a description to this task: ", validators=[DataRequired()])
    submit = SubmitField("Add")