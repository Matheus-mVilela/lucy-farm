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

        assert response.json() == {
            "name": payload_item["name"],
            "price": payload_item["price"],
            "measure": payload_item["measure"],
            "id": "1",
        }

    def test_valid_saves_on_db(self, payload_item, session_maker):
        assert session_maker().query(models.Item).count() == 0

        response = client.post(self.build_url(), json=payload_item)
        assert response.ok

        assert session_maker().query(models.Item).count() == 1

        item = session_maker().query(models.Item).first()
        assert payload_item["name"] == item.name
        assert payload_item["price"] == item.price
        assert payload_item["measure"] == item.measure

    def test_empity_returns_unprocessable_entity(self):
        response = client.post(self.build_url(), json={})
        assert response.status_code == 422

    def test_item_exist_returns_400(self, payload_item):
        client.post(self.build_url(), json=payload_item)
        response = client.post(self.build_url(), json=payload_item)
        assert response.status_code == 400
        assert response.json() == {"detail": "Item already exist."}


@pytest.mark.usefixtures("use_db")
class TestDetailItem:
    def build_url(self, name):
        return f"{URL}/item/{name}"

    def test_valid_returns_200(self, item_fixture):
        request = client.get(self.build_url(item_fixture.item.name))
        assert request.status_code == 200

    def test_valid_returns_comple_body(self, item_fixture):
        request = client.get(self.build_url(item_fixture.item.name))
        assert request.json() == {
            "name": item_fixture.item.name,
            "price": item_fixture.item.price,
            "measure": item_fixture.item.measure,
            "id": "1",
        }

    def test_unexist_item_returns_404(self):
        request = client.get(self.build_url("fake_name_item"))
        assert request.status_code == 404
        assert request.json() == {"detail": "Item does not exist."}

    def test_valid_is_same_info_on_db(self, item_fixture, session_maker):
        request = client.get(self.build_url(item_fixture.item.name))
        item = session_maker().query(models.Item).first()
        assert request.json() == {
            "name": item_fixture.item.name,
            "price": item_fixture.item.price,
            "measure": item_fixture.item.measure,
            "id": "1",
        }


@pytest.mark.usefixtures("use_db")
class TestUpdateItem:
    def build_url(self, name):
        return f"{URL}/item/{name}"

    def test_exist_item_returns_200(self, item_fixture):
        request = client.get(self.build_url(item_fixture.item.name))
        assert request.status_code == 200

    def test_modifi_item(self, payload_item):
        request = client.post(self.build_url(payload_item))

        assert request.json()
