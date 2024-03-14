from datetime import datetime, timedelta
import unittest
from SoftwareDevelopmingMethodologies.Models import Master, Client, Service, Timetable
from SoftwareDevelopmingMethodologies.Models.Appointment import Appointment


class TestAppointment(unittest.TestCase):
    def test_validate_service(self):
        self.appointment_data1 = {
            "id": 1,
            "status": "Запланирована",
            "date_and_time": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Ногтевой сервис", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment1 = Appointment(**self.appointment_data1)
        self.appointment_data2 = {
            "id": 2,
            "status": "Запланирована",
            "date_and_time": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Парикмахерские услуги", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment2 = Appointment(**self.appointment_data2)
        # Проверка метода validate_service при корректных данных
        self.assertTrue(self.appointment1.validate_service())
        # Проверка метода validate_service при некорректных данных
        with self.assertRaises(ValueError):
            self.appointment2.validate_service()

    def test_validate_future_date_and_time(self):
        self.appointment_data1 = {
            "id": 1,
            "status": "Запланирована",
            "date_and_time": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Ногтевой сервис", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment1 = Appointment(**self.appointment_data1)
        self.appointment_data2 = {
            "id": 2,
            "status": "Запланирована",
            "date_and_time": (datetime.now()).strftime("%Y-%m-%d %H:%M"),
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Парикмахерские услуги", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment2 = Appointment(**self.appointment_data2)
        # Проверка метода validate_future_date_and_time при корректных данных
        self.assertTrue(self.appointment1.validate_future_date_and_time())
        # Проверка метода validate_future_date_and_time при некорректных данных
        with self.assertRaises(ValueError):
            self.appointment2.validate_future_date_and_time()

    def test_validate_past_date_and_time(self):
        self.appointment_data1 = {
            "id": 1,
            "status": "Выполнена",
            "date_and_time": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Ногтевой сервис", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment1 = Appointment(**self.appointment_data1)
        self.appointment_data2 = {
            "id": 2,
            "status": "Выполнена",
            "date_and_time": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Парикмахерские услуги", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment2 = Appointment(**self.appointment_data2)
        # Проверка метода validate_past_date_and_time при корректных данных
        self.assertTrue(self.appointment1.validate_past_date_and_time())
        # Проверка метода validate_past_date_and_time при некорректных данных
        with self.assertRaises(ValueError):
            self.appointment2.validate_past_date_and_time()

    def test_validate_appointment_timing(self):
        self.appointment_data1 = {
            "id": 1,
            "status": "Запланирована",
            "date_and_time": "2024-03-25 10:00",
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Парикмахерские услуги", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment1 = Appointment(**self.appointment_data1)
        self.appointment_data2 = {
            "id": 2,
            "status": "Запланирована",
            "date_and_time": "2024-03-28 10:00",
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Парикмахерские услуги", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment2 = Appointment(**self.appointment_data2)
        timetable = Timetable.Timetable(id=1, day_of_week="Monday", hours=["09:00 - 18:00"], master=self.appointment1.master)
        self.appointment1.timetables[1] = timetable
        self.appointment2.timetables[1] = timetable
        # Проверка метода validate_appointment_timing при корректных данных
        self.assertTrue(self.appointment1.validate_appointment_timing())
        # Проверка метода validate_appointment_timing при некорректных данных
        with self.assertRaises(ValueError):
            self.appointment2.validate_appointment_timing()

    def test_validate_client_appointment_relationship(self):
        self.appointment_data1 = {
            "id": 1,
            "status": "Запланирована",
            "date_and_time": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Парикмахерские услуги", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment1 = Appointment(**self.appointment_data1)
        self.appointment_data2 = {
            "id": 1,
            "status": "Запланирована",
            "date_and_time": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "master": Master.Master(id=1, first_name="Алина", last_name="Морковкина", phone_number="123456789",
                                    speciality="Парикмахерские услуги", category="Профи"),
            "client": Client.Client(id=1, first_name="Светлана", last_name="Сидорова", phone_number="987654321"),
            "service": Service.Service(service_name="Маникюр",
                                       description="Снятие покрытия, опил формы, нанесение нового покрытия", price=90,
                                       speciality="Ногтевой сервис", category="Профи")
        }
        self.appointment2 = Appointment(**self.appointment_data2)
        self.appointment1.appointments[self.appointment1.id] = self.appointment1
        # Записываем клиента на ту же процедуру
        self.appointment1.appointments[self.appointment1.id + 1] = self.appointment2
        # Проверяем, что вызывается исключение ValueError
        with self.assertRaises(ValueError):
            self.appointment1.validate_client_appointment_relationship()


if __name__ == '__main__':
    unittest.main()