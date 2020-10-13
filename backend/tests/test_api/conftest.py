import uuid
import random
import collections

import pytest

from app import models


@pytest.fixture
def payload_user():
    return {'username': 'root', 'email': 'root@email.com', 'password': '123'}


@pytest.fixture
def user_fixture(session_maker):
    session = session_maker()

    user = models.User(
        username='Rick',
        email='wubbaLubbaDubDub@sanchez.com',
        hashed_password=str(uuid.uuid4()),
    )
    session.add(user)
    session.flush()
    session.commit()

    info = collections.namedtuple('info', 'user session')
    return info(user=user, session=session)


@pytest.fixture
def payload_item():
    return {
        'name': f'Leite-{uuid.uuid4()}',
        'price': round(random.uniform(1, 999), 2),
        'measure': str(uuid.uuid4()),
    }
