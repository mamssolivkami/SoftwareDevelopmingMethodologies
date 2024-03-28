from dataclasses import dataclass
from SoftwareDevelopmingMethodologies.Models.Category import Category
from SoftwareDevelopmingMethodologies.Models.Speciality import Speciality


@dataclass(frozen=True)
class Service:
    service_name: str
    description: str
    price: int
    speciality: Speciality
    category: Category
