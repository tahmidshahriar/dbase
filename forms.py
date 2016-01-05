from flask.ext.wtf import Form
from wtforms.fields import TextField
class TodoForm(Form):
    todo = TextField('todo')
