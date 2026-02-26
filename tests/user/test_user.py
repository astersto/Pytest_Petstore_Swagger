import pytest
from models.user_model import User

class TestUser:

    @pytest.mark.smoke
    def test_create_user(self, user_service, user_data):
        for data in user_data:
            user = User(
                id=data["id"],
                username=data["username"],
                firstName=data["firstName"],
                lastName=data["lastName"],
                email=data["email"],
                password=data["password"],
                phone=data["phone"],
                userStatus=data["userStatus"]
            )
            response = user_service.create_user(user.to_dict())
            assert response.status_code == 200

    @pytest.mark.smoke
    def test_login_user(self, user_service, user_data):
        for data in user_data:
            response = user_service.login_user(data["username"], data["password"])
            assert response.status_code == 200

    @pytest.mark.regression
    def test_get_user(self, user_service, user_data):
        for data in user_data:
            response = user_service.get_user(data["username"])
            assert response.status_code == 200
            assert response.json()["username"] == data["username"]

    @pytest.mark.regression
    def test_update_user(self, user_service, user_data):
        for data in user_data:
            data["firstName"] = "Updated_" + data["firstName"]
            user = User(
                id=data["id"],
                username=data["username"],
                firstName=data["firstName"],
                lastName=data["lastName"],
                email=data["email"],
                password=data["password"],
                phone=data["phone"],
                userStatus=data["userStatus"]
            )
            response = user_service.update_user(data["username"], user.to_dict())
            assert response.status_code == 200

    @pytest.mark.regression
    def test_logout_user(self, user_service):
        response = user_service.logout_user()
        assert response.status_code == 200

    @pytest.mark.regression
    def test_delete_user(self, user_service, user_data):
        for data in user_data:
            response = user_service.delete_user(data["username"])
            assert response.status_code == 200
