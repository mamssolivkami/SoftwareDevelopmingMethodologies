from SoftwareDevelopmingMethodologies.Models.Appointment import Appointment
from SoftwareDevelopmingMethodologies.Models.Category import Category
from SoftwareDevelopmingMethodologies.Models.Client import Client
from SoftwareDevelopmingMethodologies.Models.Master import Master
from SoftwareDevelopmingMethodologies.Models.Service import Service
from SoftwareDevelopmingMethodologies.Models.Timetable import Timetable
from Repositories.AppointmentRepository import AppointmentRepository
from Repositories.CategoryRepository import CategoryRepository
from Repositories.ClientRepository import ClientRepository
from Repositories.FakeRepository import FakeRepository
from Repositories.MasterRepository import MasterRepository
from Repositories.ServiceRepository import ServiceRepository
from Repositories.TimetableRepository import TimetableRepository
from Repositories.SpecialityRepository import SpecialityRepository

fake_repository = FakeRepository()
appointment_repo = AppointmentRepository()
category_repo = CategoryRepository()
client_repo = ClientRepository()
master_repo = MasterRepository()
service_repo = ServiceRepository()
speciality_repo = SpecialityRepository()
timetable_repo = TimetableRepository()

fake_repository.register_repository(appointment_repo)
fake_repository.register_repository(client_repo)
fake_repository.register_repository(category_repo)
fake_repository.register_repository(master_repo)
fake_repository.register_repository(service_repo)
fake_repository.register_repository(speciality_repo)
fake_repository.register_repository(timetable_repo)

# Создание экземпляров мастеров, клиентов, категорий, услуг, записей на прием и расписания
master1 = Master(1, "Иван", "Иванов", "123456789", "Парикмахерие услуги", 1)
master2 = Master(2, "Анна", "Петрова", "987654321", "Ногтевой сервис", 2)

client1 = Client(1, "Екатерина", "Сидорова", "111222333")
client2 = Client(2, "Александр", "Козлов", "444555666")

category1 = Category("Новичок")
category2 = Category("Эксперт")

service1 = Service("Стрижка в модном стиле", "Стрижка по последним трендам", 50.0, 1, 1)
service2 = Service("Классический маникюр", "Комплекс услуг по уходу за ногтями", 30.0, 2, 2)

category1 = Category("Парикмахерие услуги")
category2 = Category("Ногтевой сервис")

appointment1 = Appointment(1, "Запланировано", "2024-03-11 10:00", master1, client1, service1)
appointment2 = Appointment(2, "Завершено", "2024-03-12 15:30", master2, client2, service2)

timetable1 = Timetable(1, "Понедельник", "10:00 - 18:00", master1)
timetable2 = Timetable(2, "Вторник", "12:00 - 20:00", master2)

fake_repository.add_entity(appointment1)
fake_repository.add_entity(appointment2)
fake_repository.add_entity(master1)
fake_repository.add_entity(master2)
fake_repository.add_entity(client1)
fake_repository.add_entity(client2)
fake_repository.add_entity(category1)
fake_repository.add_entity(category2)
fake_repository.add_entity(service1)
fake_repository.add_entity(service2)
fake_repository.add_entity(timetable1)
fake_repository.add_entity(timetable2)

appointment = fake_repository.get_entity_by_id(1)
print(appointment.client.first_name, appointment.client.last_name,
      appointment.master.first_name, appointment.master.last_name,
      appointment.service.service_name, appointment.service.price,
      appointment.date_and_time, appointment.status)
