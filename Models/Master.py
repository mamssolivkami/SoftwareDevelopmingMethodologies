from SoftwareDevelopmingMethodologies.Models.Service import Service


class Master:
    def __init__(self, id, first_name, last_name, phone_number, speciality, category):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.speciality = speciality
        self.category = category

    def __eq__(self, other):
        if not isinstance(other, Master):
            return False
        return (self.id == other.id and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.phone_number == other.phone_number and
                self.speciality == other.speciality and
                self.category == other.category)

    def can_provide_service(self, service: Service) -> bool:
        return service.speciality == self.speciality and service.category == self.category
