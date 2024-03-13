import unittest
from datetime import datetime
from Repositories import AppointmentRepository
from Models import Appointment, Timetable, Master, Service, Client


class TestAppointmentRepository(unittest.TestCase):
    def setUp(self):
        self.appointment_repo = AppointmentRepository.AppointmentRepository()

    def test_validate_service(self):
        master = Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                               speciality="Парикмахерские услуги", category="Профи")
        client = Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321")
        service = Service.Service(service_name="Маникюр",
                                  description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                  speciality="Ногтевой сервис", category="Профи")
        timetable = Timetable.Timetable(id=1, day_of_week="Суббота", hours=["09:00 - 18:00"], master=master)

        # Создаем запись с неподходящей услугой для мастера
        appointment = Appointment.Appointment(id=1, status="Запланирована", date_and_time="2024-03-16 12:30", master=master,
                                              client=client, service=service)

        with self.assertRaises(ValueError):
            self.appointment_repo.add(appointment, [timetable])

    def test_validate_future_date_and_time(self):
        # Создаем запись с прошедшей датой и временем
        master = Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                               speciality="Ногтевой сервис", category="Профи")
        client = Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321")
        service = Service.Service(service_name="Маникюр",
                                  description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                  speciality="Ногтевой сервис", category="Профи")
        appointment = Appointment.Appointment(id=1, status="Запланирована", date_and_time="2024-03-11 12:00",
                                               master=master,
                                               client=client, service=service)
        timetable = Timetable.Timetable(id=1, day_of_week="Понедельник", hours=["09:00 - 18:00"], master=master)

        with self.assertRaises(ValueError):
            self.appointment_repo.add(appointment, [timetable])

    def test_validate_past_date_and_time(self):
        # Создаем запись с будущей датой и временем
        master = Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                               speciality="Ногтевой сервис", category="Профи")
        client = Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321")
        service = Service.Service(service_name="Маникюр",
                                  description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                  speciality="Ногтевой сервис", category="Профи")
        appointment = Appointment.Appointment(id=1, status="Выполнена", date_and_time="2024-03-28 12:00",
                                               master=master,
                                               client=client, service=service)
        timetable = Timetable.Timetable(id=1, day_of_week="Понедельник", hours=["09:00 - 18:00"], master=master)

        with self.assertRaises(ValueError):
            self.appointment_repo.add(appointment, [timetable])

    def test_validate_appointment_timing(self):
        # Создаем расписание работы мастера на понедельник с 9:00 до 18:00
        master = Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                               speciality="Ногтевой сервис", category="Профи")
        client = Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321")
        service = Service.Service(service_name="Маникюр",
                                  description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                  speciality="Ногтевой сервис", category="Профи")
        timetable = Timetable.Timetable(id=1, day_of_week="Monday", hours=["09:00 - 18:00"], master=master)

        # Создаем запись на понедельник в 10:00
        appointment = Appointment.Appointment(id=1, status="Запланирована", date_and_time="2024-03-25 10:00",
                                              master=master,
                                              client=client, service=service)

        # Проверяем, что при вызове метода add не возникает исключений
        try:
            self.appointment_repo.add(appointment, [timetable])
        except ValueError as e:
            self.fail(f"Было вызвано исключение: {e}")


if __name__ == '__main__':
    unittest.main()
