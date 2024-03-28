from SoftwareDevelopmingMethodologies.Models.Client import Client


class ClientRepository:
    def __init__(self):
        self.entity_class = Client
        self.clients = {}

    def add(self, client):
        self.clients[client.id] = client

    def get_by_id(self, client_id):
        return self.clients.get(client_id)
