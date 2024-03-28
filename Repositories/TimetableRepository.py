from SoftwareDevelopmingMethodologies.Models.Timetable import Timetable


class TimetableRepository:
    def __init__(self):
        self.entity_class = Timetable
        self.timetables = {}

    def add(self, timetable):
        self.timetables[timetable.id] = timetable

    def get_by_id(self, timetable_id):
        return self.timetables.get(timetable_id)
