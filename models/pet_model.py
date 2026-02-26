from dataclasses import dataclass,field
from typing import List

@dataclass
class Category:
    id: int = 0
    name: str = ""

@dataclass
class Tag:
    id: int = 0
    name: str = ""

@dataclass
class Pet:
    id: int = 0
    name: str = ""
    photoUrls:  List[str] = field(default_factory=list)
    category: Category = field(default_factory=Category)
    tags: List[Tag] = field(default_factory=list)
    status: str = "available"

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "photoUrls" : self.photoUrls,
            "category" : {"id" : self.category.id, "name" : self.category.name},
            "tags" : [{"id" : t.id, "name" : t.name} for t in self.tags],
            "status" : self.status
        }
