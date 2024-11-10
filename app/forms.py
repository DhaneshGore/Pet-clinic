from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class OwnerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    contact = StringField('Contact')
    submit = SubmitField('Add Owner')

class PetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    owner_id = IntegerField('Owner ID', validators=[DataRequired()])
    submit = SubmitField('Add Pet')

class AppointmentForm(FlaskForm):
    date = DateTimeField('Date', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
    pet_id = IntegerField('Pet ID', validators=[DataRequired()])
    submit = SubmitField('Add Appointment')
