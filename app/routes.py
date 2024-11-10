from flask import Blueprint, render_template, request, redirect, url_for
from app import db  # Import db from app, avoiding circular import
from app.models import Owner, Pet, Appointment
from datetime import datetime
from app.models import Owner, Pet, Appointment


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    owners = Owner.query.order_by(Owner.name).all()
    return render_template('index.html', owners=owners)

@bp.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        new_owner = Owner(name=name, contact=contact)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_owner.html')

@bp.route('/pets')
def list_pets():
    pets = Pet.query.order_by(Pet.name).all()
    return render_template('pets.html', pets=pets)

@bp.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        owner_id = request.form['owner_id']
        new_pet = Pet(name=name, type=type, owner_id=owner_id)
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('main.list_pets'))
    owners = Owner.query.all()
    return render_template('add_pet.html', owners=owners)

@bp.route('/appointments')
def list_appointments():
    appointments = Appointment.query.order_by(Appointment.date).all()
    return render_template('appointments.html', appointments=appointments)

@bp.route('/add_appointment', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        date = request.form['date']
        pet_id = request.form['pet_id']
        new_appointment = Appointment(date=datetime.strptime(date, '%Y-%m-%d'), pet_id=pet_id)
        db.session.add(new_appointment)
        db.session.commit()
        return redirect(url_for('main.list_appointments'))
    pets = Pet.query.all()
    return render_template('add_appointment.html', pets=pets)
