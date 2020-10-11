import pytest
from fastapi.testclient import TestClient

from app import api, models

client = TestClient(api.app)


@pytest.mark.usefixtures('use_db')
class TestCreateUser:
    def build_url(self):
        return '/api/v.1/user'

    def test_valid_returns_201(self, payload):
        response = client.post(self.build_url(), json=payload)
        assert response.status_code == 201

    def test_valid_returns_complete_body(self, payload):
        response = client.post(self.build_url(), json=payload)
        assert response.json() == {
            'username': payload['username'],
            'email': payload['email'],
        }

    def test_valid_saves_on_db(self, payload, session_maker):
        assert session_maker().query(models.User).count() == 0

        response = client.post(self.build_url(), json=payload)
        assert response.ok

        assert session_maker().query(models.User).count() == 1

        user = session_maker().query(models.User).first()
        assert payload['username'] == user.username
        assert payload['email'] == user.email
        # TODO:
        # assert security.verify_password(
        #     payload['password'], user.hashed_password
        # )
