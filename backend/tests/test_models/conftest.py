import uuid
import pytest


@pytest.fixture
def payload():
    return {
        'username': 'Rick',
        'email': 'wubbaLubbaDubDub@sanchez.com',
        'hashed_password': str(uuid.uuid4()),
    }
