from datetime import datetime


class AppointmentRepository:
    def __init__(self):
        self.appointments = {}

    def add(self, appointment, timetables):
        self.validate_service(appointment)
        self.validate_future_date_and_time(appointment)
        self.validate_past_date_and_time(appointment)
        self.validate_appointment_timing(appointment, timetables)
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

    @staticmethod
    def validate_appointment_timing(appointment, timetables):
        # Получаем день недели из даты записи
        appointment_date = datetime.strptime(appointment.date_and_time, "%Y-%m-%d %H:%M")
        appointment_weekday = appointment_date.strftime("%A")

        # Ищем расписание работы мастера на этот день
        for timetable in timetables:
            if timetable.master == appointment.master and timetable.day_of_week == appointment_weekday:
                # Проверяем, что время записи попадает в интервалы работы мастера
                appointment_time = appointment_date.time()
                for interval in timetable.hours:
                    start_time, end_time = interval.split(" - ")
                    start_time = datetime.strptime(start_time, "%H:%M").time()
                    end_time = datetime.strptime(end_time, "%H:%M").time()
                    if start_time <= appointment_time <= end_time:
                        return  # Запись валидна
                raise ValueError("Выбранный мастер не работает в это время")
        raise ValueError("Выбранный мастер не работает в этот день")
