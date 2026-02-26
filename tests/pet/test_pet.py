import pytest
from models.pet_model import Pet, Category, Tag

class TestPet:

    @pytest.mark.smoke
    def test_add_pet(self,pet_service,pet_data):
        for data in pet_data:
            pet = Pet(
                id = data["id"],
                name = data["name"],
                status = data["status"],
                category = Category(**data["category"]),
                tags = [Tag(**t) for t in data["tags"]],
                photoUrls = data["photoUrls"]
            )
            response = pet_service.add_pet(pet.to_dict())
            assert response.status_code == 200
            assert response.json()["name"] == pet.name

    @pytest.mark.smoke
    def test_get_pet_by_id(self, pet_service, pet_data):
        for data in pet_data:
            response = pet_service.get_pet_by_id(data["id"])
            assert response.status_code == 200
            assert response.json()["id"] == data["id"]

    @pytest.mark.regression
    def test_get_pet_by_status(self, pet_service, pet_data):
        for data in pet_data:
            response = pet_service.get_pet_by_status(data["status"])
            assert response.status_code == 200

    @pytest.mark.regression
    def test_update_pet(self, pet_service, pet_data):
        for data in pet_data:
            data["name"] = "Updated_" + data["name"]
            pet = Pet(
                id=data["id"],
                name=data["name"],
                status=data["status"],
                category=Category(**data["category"]),
                tags=[Tag(**t) for t in data["tags"]],
                photoUrls=data["photoUrls"]
            )
            response = pet_service.update_pet(pet.to_dict())
            assert response.status_code == 200
            assert response.json()["name"] == pet.name

    @pytest.mark.regression
    def test_delete_pet(self, pet_service, pet_data):
        for data in pet_data:
            response = pet_service.delete_pet(data["id"])
            assert response.status_code == 200