import requests


class PetstoreClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def create_user(self, payload: dict) -> requests.Response:
        return requests.post(f"{self.base_url}/user", json=payload)

    def get_user(self, username: str) -> requests.Response:
        return requests.get(f"{self.base_url}/user/{username}")
