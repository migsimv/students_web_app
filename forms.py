from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email 

class StudentForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = IntegerField('Age')
    birth_date = DateField('Birth Date')
    active = BooleanField('Active', default=True)
    submit = SubmitField('Submit')
