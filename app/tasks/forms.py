from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, validators

class CreateTaskForm(Form):
    title = TextField('Title', [validators.Required()])
    description = TextField('Description', [validators.Required(), validators.length(max=200)])