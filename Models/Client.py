class Client:
    def __init__(self, id, first_name, last_name, phone_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return (self.id == other.id and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.phone_number == other.phone_number)
