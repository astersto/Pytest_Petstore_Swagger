from base.base_test import BaseTest
from constants.endpoints import (
    ADD_PET, UPDATE_PET, GET_PET_BY_ID, GET_PET_BY_STATUS,
    UPDATE_PET_BY_ID, DELETE_PET
)

class PetService(BaseTest):

    def add_pet(self, body):
        return self.post(ADD_PET,body)

    def update_pet(self, body):
        return self.put(UPDATE_PET,body)

    def get_pet_by_id(self, pet_id):
        return self.get(GET_PET_BY_ID.format(petId=pet_id))

    def get_pet_by_status(self, status):
        return self.get(GET_PET_BY_STATUS, params={"status" : status})

    def update_pet_by_id(self, pet_id, body):
        return self.put(UPDATE_PET_BY_ID.format(petId=pet_id), body)

    def delete_pet(self, pet_id):
        return self.delete(DELETE_PET.format(petId=pet_id))