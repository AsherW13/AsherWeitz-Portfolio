from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=1000)])
