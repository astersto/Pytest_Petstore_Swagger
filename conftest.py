import json
import pytest
import os
from services.pet_service import PetService
from services.user_service import UserService
from services.store_service import StoreService

@pytest.fixture(scope="session")
def pet_service():
    return PetService()

@pytest.fixture(scope="session")
def user_service():
    return UserService()

@pytest.fixture(scope="session")
def store_service():
    return StoreService()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope="session")
def pet_data():
    with open(os.path.join(BASE_DIR, "test_data", "pet_data.json")) as file:
        return json.load(file)

@pytest.fixture(scope="session")
def user_data():
    with open(os.path.join(BASE_DIR, "test_data", "user_data.json")) as file:
        return json.load(file)

@pytest.fixture(scope="session")
def store_data():
    with open(os.path.join(BASE_DIR, "test_data", "store_data.json")) as file:
        return json.load(file)

