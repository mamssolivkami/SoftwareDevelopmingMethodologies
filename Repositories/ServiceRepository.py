class ServiceRepository:
    def __init__(self):
        self.services = {}

    def add(self, service):
        self.services[service.id] = service

    def get_by_id(self, service_id):
        return self.services.get(service_id)
