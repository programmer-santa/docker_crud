from flask import Blueprint, request, jsonify
from ..models.appointment import Appointment
from ..services.appointment_service import AppointmentService

appointment_bp = Blueprint('appointments', __name__)

@appointment_bp.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    appointment = Appointment(**data)
    AppointmentService.create_appointment(appointment)
    return jsonify({'message': 'Appointment created successfully'}), 201

@appointment_bp.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = AppointmentService.get_all_appointments()
    return jsonify([appointment.to_dict() for appointment in appointments]), 200

@appointment_bp.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = AppointmentService.get_appointment_by_id(appointment_id)
    if appointment:
        return jsonify(appointment.to_dict()), 200
    return jsonify({'message': 'Appointment not found'}), 404

@appointment_bp.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    data = request.get_json()
    appointment = AppointmentService.update_appointment(appointment_id, **data)
    if appointment:
        return jsonify({'message': 'Appointment updated successfully'}), 200
    return jsonify({'message': 'Appointment not found'}), 404

@appointment_bp.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    success = AppointmentService.delete_appointment(appointment_id)
    if success:
        return jsonify({'message': 'Appointment deleted successfully'}), 200
    return jsonify({'message': 'Appointment not found'}), 404