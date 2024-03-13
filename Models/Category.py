from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    category_name: str
