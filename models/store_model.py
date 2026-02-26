from dataclasses import dataclass

@dataclass
class Store:
    id: int = 0
    petId: int = 0
    quantity: int = 0
    shipDate: str = ""
    status: str = ""
    complete: bool = False

    def to_dict(self):
        return {
            "id" : self.id,
            "petId" : self.petId,
            "quantity" : self.quantity,
            "shipDate" : self.shipDate,
            "status" : self.status,
            "complete" : self.complete
        }
