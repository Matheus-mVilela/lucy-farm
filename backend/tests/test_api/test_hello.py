import pytest
from fastapi.testclient import TestClient

from app import api

client = TestClient(api.app)


def test_hello():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'msg': 'Hello World'}
