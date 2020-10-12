import uuid
import pytest
import random


@pytest.fixture
def payload():
    return {
        "username": "Rick",
        "email": "wubbaLubbaDubDub@sanchez.com",
        "hashed_password": str(uuid.uuid4()),
    }


@pytest.fixture
def payload_item():
    return {
        "name": f"Leite-{uuid.uuid4()}",
        "price": round(random.uniform(1, 999), 2),
        "measure": str(uuid.uuid4()),
    }
