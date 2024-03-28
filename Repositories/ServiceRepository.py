from SoftwareDevelopmingMethodologies.Models.Service import Service


class ServiceRepository:
    def __init__(self):
        self.entity_class = Service
        self.services = {}

    def add(self, service):
        self.services[service.service_name] = service

    def get_by_id(self, service_id):
        return self.services.get(service_id)
