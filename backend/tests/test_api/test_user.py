import pytest
from fastapi.testclient import TestClient

from app import api, models, security

URL = '/api/v.1'
client = TestClient(api.app)


@pytest.mark.usefixtures('use_db')
class TestCreateUser:
    def build_url(self):
        return f'{URL}/user'

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
        assert security.verify_password(
            payload['password'], user.hashed_password
        )

    def test_empity_returns_unprocessable_entity(self):
        response = client.post(self.build_url(), json={})
        assert response.status_code == 422

    def test_user_exist_returns_400(self, payload):
        client.post(self.build_url(), json=payload)
        response = client.post(self.build_url(), json=payload)
        assert response.status_code == 400
        assert response.json() == {'detail': 'User already exist.'}

    def test_invalid_email_returns_422(self, payload):
        payload['email'] = 'fakemail'
        response = client.post(self.build_url(), json=payload)
        assert response.status_code == 422
        assert response.json() == {
            'detail': [
                {
                    'loc': ['body', 'user', 'email'],
                    'msg': 'value is not a valid email address',
                    'type': 'value_error.email',
                }
            ]
        }


@pytest.mark.usefixtures('use_db')
class TestDetailUser:
    def build_url(self, email):
        return f'{URL}/user/{email}'

    def test_valid_returns_200(self, user_fixture):
        request = client.get(self.build_url(user_fixture.user.email))
        assert request.status_code == 200

    def test_valid_returns_complete_body(self, user_fixture):
        request = client.get(self.build_url(user_fixture.user.email))
        assert request.json() == {
            'username': user_fixture.user.username,
            'email': user_fixture.user.email,
        }

    def test_unexist_email_returns_404(self):
        request = client.get(self.build_url('fakeemail@gmail.com'))
        assert request.status_code == 404
        assert request.json() == {'detail': 'User does not exist.'}

    def test_valid_is_same_info_on_db(self, user_fixture, session_maker):
        request = client.get(self.build_url(user_fixture.user.email))
        user = session_maker().query(models.User).first()
        assert request.json() == {
            'username': user.username,
            'email': user.email,
        }
