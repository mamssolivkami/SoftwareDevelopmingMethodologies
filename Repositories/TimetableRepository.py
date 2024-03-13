class TimetableRepository:
    def __init__(self):
        self.timetables = {}

    def add(self, timetable):
        self.timetables[timetable.id] = timetable

    def get_by_id(self, timetable_id):
        return self.timetables.get(timetable_id)
