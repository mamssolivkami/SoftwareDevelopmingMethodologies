from Models.Appointment import Appointment
from Models.Category import Category
from Models.Client import Client
from Models.Master import Master
from Models.Service import Service
from Models.Timetable import Timetable
from Repositories.AppointmentRepository import AppointmentRepository
from Repositories.CategoryRepository import CategoryRepository
from Repositories.ClientRepository import ClientRepository
from Repositories.FakeRepository import FakeRepository
from Repositories.MasterRepository import MasterRepository
from Repositories.ServiceRepository import ServiceRepository
from Repositories.TimetableRepository import TimetableRepository

fake_repository = FakeRepository()

fake_repository.register_repository(Appointment, AppointmentRepository())
fake_repository.register_repository(Client, ClientRepository())
fake_repository.register_repository(Category, CategoryRepository())
fake_repository.register_repository(Master, MasterRepository())
fake_repository.register_repository(Service, ServiceRepository())
fake_repository.register_repository(Timetable, TimetableRepository())

# Создание экземпляров мастеров, клиентов, категорий, услуг, записей на прием и расписания
master1 = Master(1, "Иван", "Иванов", "123456789", "Парикмахер", 1)
master2 = Master(2, "Анна", "Петрова", "987654321", "Маникюрщица", 2)

client1 = Client(1, "Екатерина", "Сидорова", "111222333")
client2 = Client(2, "Александр", "Козлов", "444555666")

category1 = Category("Новичок")
category2 = Category("Эксперт")

service1 = Service(1, "Стрижка в модном стиле", "Стрижка по последним трендам", 50.0, 1)
service2 = Service(2, "Классический маникюр", "Комплекс услуг по уходу за ногтями", 30.0, 2)

appointment1 = Appointment(1, "Запланировано", "2024-03-01 10:00", master1, client1, service1)
appointment2 = Appointment(2, "Завершено", "2024-03-02 15:30", master2, client2, service2)

timetable1 = Timetable(1, "Понедельник", "10:00 - 18:00", master1)
timetable2 = Timetable(2, "Вторник", "12:00 - 20:00", master2)

fake_repository.add_entity(Appointment, appointment1)
fake_repository.add_entity(Appointment, appointment2)
fake_repository.add_entity(Master, master1)
fake_repository.add_entity(Master, master2)
fake_repository.add_entity(Client, client1)
fake_repository.add_entity(Client, client2)
fake_repository.add_entity(Category, category1)
fake_repository.add_entity(Category, category2)
fake_repository.add_entity(Service, service1)
fake_repository.add_entity(Service, service2)
fake_repository.add_entity(Timetable, timetable1)
fake_repository.add_entity(Timetable, timetable2)

appointment = fake_repository.get_entity_by_id(Appointment, 1)
print(appointment.client.first_name, appointment.client.last_name,
      appointment.master.first_name, appointment.master.last_name,
      appointment.service.service_name, appointment.service.price,
      appointment.date_and_time, appointment.status)
