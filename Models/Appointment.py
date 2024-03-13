class Appointment:
    def __init__(self, id, status, date_and_time, master, client, service):
        self.id = id
        self.status = status
        self.date_and_time = date_and_time
        self.master = master
        self.client = client
        self.service = service

    def __eq__(self, other):
        if not isinstance(other, Appointment):
            return False
        return (self.id == other.id and
                self.status == other.status and
                self.date_and_time == other.date_and_time and
                self.master == other.master and
                self.client == other.client and
                self.service == other.service)
