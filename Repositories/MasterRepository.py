class MasterRepository:
    def __init__(self):
        self.masters = {}

    def add(self, master):
        self.masters[master.id] = master

    def get_by_id(self, master_id):
        return self.masters.get(master_id)
