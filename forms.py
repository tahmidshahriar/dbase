from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, DateField
class DataForm(Form):
    program = TextField('program')
    eligibility = TextField('eligibility')
    date = TextField('date')
    applicationDeadline = TextField('applicationDeadline')
    programHyper = TextField('programHyper')
    applicationHyper = TextField('applicationHyper')
    login = TextField('login')
    courses = TextField('applicationDeadline')
    faq = TextField('faq')
    sat = TextField('sat')
    lor = TextField('lor')
    essay = TextField('essay')
    note = TextField('note')
