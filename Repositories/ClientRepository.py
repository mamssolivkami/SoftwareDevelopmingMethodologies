class ClientRepository:
    def __init__(self):
        self.clients = {}

    def add(self, client):
        self.clients[client.id] = client

    def get_by_id(self, client_id):
        return self.clients.get(client_id)
