import pytest
from models.store_model import Store

class TestStore:

    @pytest.mark.smoke
    def test_place_order(self, store_service, store_data):
        for data in store_data:
            store = Store(
                id=data["id"],
                petId=data["petId"],
                quantity=data["quantity"],
                shipDate=data["shipDate"],
                status=data["status"],
                complete=data["complete"]
            )
            response = store_service.place_order(store.to_dict())
            assert response.status_code == 200
            assert response.json()["petId"] == store.petId

    @pytest.mark.smoke
    def test_get_order_by_id(self, store_service, store_data):
        for data in store_data:
            response = store_service.get_order_by_id(data["id"])
            assert response.status_code == 200
            assert response.json()["id"] == data["id"]

    @pytest.mark.regression
    def test_get_inventory(self, store_service):
        response = store_service.get_inventory()
        assert response.status_code == 200

    @pytest.mark.regression
    def test_delete_order(self, store_service, store_data):
        for data in store_data:
            response = store_service.delete_order(data["id"])
            assert response.status_code == 200
