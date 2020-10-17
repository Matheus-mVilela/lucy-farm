import pytest
from fastapi import testclient

from app import api, models

URL = "/api/v.1"
client = testclient.TestClient(api.app)


@pytest.mark.usefixtures("use_db")
class TestCreateItem:
    def build_url(self):
        return f"{URL}/item"

    def test_valid_returns_201(self, payload_item):
        response = client.post(self.build_url(), json=payload_item)
        assert response.status_code == 201

    def test_valid_returns_complete_body(self, payload_item):
        response = client.post(self.build_url(), json=payload_item)

        breakpoint()

        assert response.json() == {
            "name": payload_item["name"],
            "price": payload_item["price"],
            "measure": payload_item["measure"],
            "id": "1",
        }
