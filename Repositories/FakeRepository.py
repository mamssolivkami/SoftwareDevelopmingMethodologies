class FakeRepository:
    def __init__(self):
        self.entities = {}

    def register_repository(self, repository_instance):
        entity_class = repository_instance.entity_class
        self.entities[entity_class] = repository_instance

    def add_entity(self, entity):
        entity_class = type(entity)
        repository = self.entities.get(entity_class)
        if repository:
            repository.add(entity)
        else:
            raise ValueError(f"No repository registered for {entity_class}")

    def get_entity_by_id(self, entity_id):
        for repository in self.entities.values():
            entity = repository.get_by_id(entity_id)
            if entity:
                return entity
        raise ValueError(f"No entity found with id {entity_id}")
