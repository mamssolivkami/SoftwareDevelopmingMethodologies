from datetime import datetime


class Appointment:
    def __init__(self, id, status, date_and_time, master, client, service):
        self.id = id
        self.status = status
        self.date_and_time = date_and_time
        self.master = master
        self.client = client
        self.service = service
        self.appointments = {}
        self.timetables = {}

    def __eq__(self, other):
        if not isinstance(other, Appointment):
            return False
        return (self.id == other.id and
                self.status == other.status and
                self.date_and_time == other.date_and_time and
                self.master == other.master and
                self.client == other.client and
                self.service == other.service)

    def validate_service(self):
        if not self.master.can_provide_service(self.service):
            raise ValueError("Услуга не может быть оказана мастером этой специализации или категории")
        return True

    def validate_future_date_and_time(self):
        if self.status == "Запланирована":
            appointment_datetime = datetime.strptime(self.date_and_time, "%Y-%m-%d %H:%M")
            if appointment_datetime <= datetime.now():
                raise ValueError("Дата и время записи должны быть в будущем")
        return True

    def validate_past_date_and_time(self):
        if self.status == "Выполнена":
            appointment_datetime = datetime.strptime(self.date_and_time, "%Y-%m-%d %H:%M")
            if appointment_datetime >= datetime.now():
                raise ValueError("Дата и время записи должны быть в прошедшем")
        return True

    def validate_appointment_timing(self):
        appointment_date = datetime.strptime(self.date_and_time, "%Y-%m-%d %H:%M")
        appointment_weekday = appointment_date.strftime("%A")

        timetable = self.timetables.get(self.master.id)
        if timetable:
            if timetable.day_of_week == appointment_weekday:
                appointment_time = appointment_date.time()
                for interval in timetable.hours:
                    start_time, end_time = interval.split(" - ")
                    start_time = datetime.strptime(start_time, "%H:%M").time()
                    end_time = datetime.strptime(end_time, "%H:%M").time()
                    if start_time <= appointment_time <= end_time:
                        return True
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
        return True
