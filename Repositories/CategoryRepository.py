from SoftwareDevelopmingMethodologies.Models.Category import Category


class CategoryRepository:
    def __init__(self):
        self.entity_class = Category
        self.categories = {}

    def add(self, category):
        self.categories[category.category_name] = category

    def get_by_id(self, category_name):
        return self.categories.get(category_name)
