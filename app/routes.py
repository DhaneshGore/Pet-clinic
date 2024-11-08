from flask import Blueprint, render_template
from app.models import Owner, Pet, Appointment
from flask import render_template

# Define the Blueprint for routes
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    owners = Owner.query.order_by(Owner.name).all()
    return render_template('index.html', owners=owners)

@bp.route('/pets')
def list_pets():
    pets = Pet.query.order_by(Pet.name).all()
    return render_template('pets.html', pets=pets)

@bp.route('/appointments')
def list_appointments():
    appointments = Appointment.query.order_by(Appointment.date).all()
    return render_template('appointments.html', appointments=appointments)
