from app.models.appointment import Appointment
from app import db

def create_appointment(date, time, client_name):
    new_appointment = Appointment(date=date, time=time, client_name=client_name)
    db.session.add(new_appointment)
    db.session.commit()
    return new_appointment

def get_appointment(appointment_id):
    return Appointment.query.get(appointment_id)

def update_appointment(appointment_id, date, time, client_name):
    appointment = get_appointment(appointment_id)
    if appointment:
        appointment.date = date
        appointment.time = time
        appointment.client_name = client_name
        db.session.commit()
    return appointment

def delete_appointment(appointment_id):
    appointment = get_appointment(appointment_id)
    if appointment:
        db.session.delete(appointment)
        db.session.commit()
    return appointment