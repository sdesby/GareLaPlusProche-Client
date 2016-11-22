from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class AddressForm(Form):
    address = StringField('address', validators=[DataRequired()])
