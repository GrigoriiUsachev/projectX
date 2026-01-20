import pytest
from api.clients.petstore_client import PetstoreClient
from shared.config.config import Config
from shared.utils.data_generator import unique_username


pytestmark = pytest.mark.api


def test_create_and_get_user():
    client = PetstoreClient(Config.PETSTORE_BASE_URL)

    username = unique_username()
    payload = {
        "id": 1,
        "username": username,
        "firstName": "ProjectX",
        "lastName": "User",
        "email": "projectx_user_001@example.com",
        "password": "pass123",
        "phone": "123456",
        "userStatus": 0
    }

    r_create = client.create_user(payload)
    assert r_create.status_code in (200, 201)

    r_get = client.get_user(username)
    assert r_get.status_code == 200
    assert r_get.json()["username"] == username
