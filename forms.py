from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, DateField
class DataForm(Form):
    program = TextField('program')
    category = TextField('category')
    location = TextField('location')
    description = TextField('description')
    eligibility = TextField('eligibility')
    date = TextField('date')
    duration = TextField('duration')
    applicationDeadline = TextField('applicationDeadline')
    essay = TextField('essay')
    programHyper = TextField('programHyper')
    applicationHyper = TextField('applicationHyper')
    reviewHyper = TextField('reviewHyper')
    top = TextField('top')
    collegeCredit = TextField('collegeCredit')
    #login = TextField('login')
    courses = TextField('courses')
    #faq = TextField('faq')
    #sat = TextField('sat')
    #lor = TextField('lor')
    note = TextField('note')

class LoginForm(Form):
    username = TextField('username')
    password = PasswordField('password')


class ChangeLoginForm(Form):
    username = TextField('username')
    password = PasswordField('password')
    newPassword = PasswordField('newPassword')
    newPassword2 = PasswordField('newPassword2')


