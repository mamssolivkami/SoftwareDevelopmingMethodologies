class FakeRepository:
    def __init__(self):
        self.entities = {}

    def register_repository(self, entity_class, repository_instance):
        self.entities[entity_class] = repository_instance

    def add_entity(self, entity_class, entity):
        repository = self.entities.get(entity_class)
        if repository:
            repository.add(entity)
        else:
            raise ValueError(f"No repository registered for {entity_class}")

    def get_entity_by_id(self, entity_class, entity_id):
        repository = self.entities.get(entity_class)
        if repository:
            return repository.get_by_id(entity_id)
        else:
            raise ValueError(f"No repository registered for {entity_class}")