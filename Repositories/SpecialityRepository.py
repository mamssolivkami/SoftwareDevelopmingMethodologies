from SoftwareDevelopmingMethodologies.Models.Speciality import Speciality


class SpecialityRepository:
    def __init__(self):
        self.entity_class = Speciality
        self.specialities = {}

    def add(self, speciality):
        self.specialities[speciality.speciality_name] = speciality

    def get_by_id(self, speciality_name):
        return self.specialities.get(speciality_name)
