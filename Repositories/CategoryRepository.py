class CategoryRepository:
    def __init__(self):
        self.categories = {}

    def add(self, category):
        self.categories[category.id] = category

    def get_by_id(self, category_id):
        return self.categories.get(category_id)
