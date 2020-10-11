import pytest


@pytest.fixture
def payload():
    return {'username': 'root', 'email': 'root@email.com', 'password': '123'}
