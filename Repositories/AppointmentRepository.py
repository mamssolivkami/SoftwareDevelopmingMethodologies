from SoftwareDevelopmingMethodologies.Models.Appointment import Appointment


class AppointmentRepository:
    def __init__(self):
        self.entity_class = Appointment
        self.appointments = {}

    def add(self, appointment):
        appointment.appointments[appointment.id] = appointment

    def get_by_id(self, appointment_id):
        return self.appointments.get(appointment_id)
