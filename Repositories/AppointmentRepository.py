from datetime import datetime


class AppointmentRepository:
    def __init__(self):
        self.appointments = {}
        self.timetables = {}

    def add(self, appointment):
        self.validate_service(appointment)
        self.validate_future_date_and_time(appointment)
        self.validate_past_date_and_time(appointment)
        self.validate_appointment_timing(appointment)
        self.validate_client_appointment_relationship()
        self.appointments[appointment.id] = appointment

    def get_by_id(self, appointment_id):
        return self.appointments.get(appointment_id)

    @staticmethod
    def validate_service(appointment):
        if not appointment.master.can_provide_service(appointment.service):
            raise ValueError("Услуга не может быть оказана мастером этой специализации или категории")

    @staticmethod
    def validate_future_date_and_time(appointment):
        if appointment.status == "Запланирована":
            appointment_datetime = datetime.strptime(appointment.date_and_time, "%Y-%m-%d %H:%M")
            if appointment_datetime <= datetime.now():
                raise ValueError("Дата и время записи должны быть в будущем")

    @staticmethod
    def validate_past_date_and_time(appointment):
        if appointment.status == "Выполнена":
            appointment_datetime = datetime.strptime(appointment.date_and_time, "%Y-%m-%d %H:%M")
            if appointment_datetime >= datetime.now():
                raise ValueError("Дата и время записи должны быть в прошедшем")

    def validate_appointment_timing(self, appointment):
        appointment_date = datetime.strptime(appointment.date_and_time, "%Y-%m-%d %H:%M")
        appointment_weekday = appointment_date.strftime("%A")

        timetable = self.timetables.get(appointment.master.id)
        if timetable:
            if timetable.day_of_week == appointment_weekday:
                appointment_time = appointment_date.time()
                for interval in timetable.hours:
                    start_time, end_time = interval.split(" - ")
                    start_time = datetime.strptime(start_time, "%H:%M").time()
                    end_time = datetime.strptime(end_time, "%H:%M").time()
                    if start_time <= appointment_time <= end_time:
                        return
                raise ValueError("Выбранный мастер не работает в это время")
        raise ValueError("Выбранный мастер не работает в этот день")

    def validate_client_appointment_relationship(self):
        appointments_copy = dict(self.appointments)  # Создаем копию словаря
        for app in appointments_copy.values():
            # Создаем ключ для клиента, игнорируя id, чтобы проверить уникальность записи
            client_key = (app.status, app.date_and_time, app.master.id, app.client.id, app.service.service_name)
            if client_key in self.appointments:
                raise ValueError("Клиент уже записан на эту процедуру")
            self.appointments[client_key] = app

