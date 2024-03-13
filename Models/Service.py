from dataclasses import dataclass
from Models import Category


@dataclass(frozen=True)
class Service:
    service_name: str
    description: str
    price: int
    speciality: str
    category: Category
