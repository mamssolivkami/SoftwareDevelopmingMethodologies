class Timetable:
    def __init__(self, id, day_of_week, hours, master):
        self.id = id
        self.day_of_week = day_of_week
        self.hours = hours
        self.master = master

    def __eq__(self, other):
        if not isinstance(other, Timetable):
            return False
        return (self.id == other.id and
                self.day_of_week == other.day_of_week and
                self.hours == other.hours and
                self.master == other.master)
