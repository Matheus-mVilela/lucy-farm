import collections

import pytest
from fastapi.testclient import TestClient

from app import api, models


URL = '/api/v.1'
client = TestClient(api.app)


@pytest.fixture
def _create_fake_user_and_item(payload_user, payload_item, session_maker):
    session = session_maker()

    user = models.User(
        username=payload_user['username'],
        email=payload_user['email'],
        hashed_password=payload_user['password'],
    )
    item = models.Item(
        name=payload_item['name'],
        price=payload_item['price'],
        measure=payload_item['measure'],
    )

    session.add(user)
    session.add(item)
    session.flush()
    session.commit()

    info = collections.namedtuple('info', 'user item')
    return info(user=user, item=item)


@pytest.fixture
def _payload(_create_fake_user_and_item):
    return {
        'user_id': _create_fake_user_and_item.user.id,
        'item_id': _create_fake_user_and_item.item.id,
    }


@pytest.mark.usefixtures('use_db')
class TestCreateOrder:
    def build_url(self):
        return f'{URL}/order'

    def test_valid_returns_201(self, _payload):
        response = client.post(self.build_url(), json=_payload)
        assert response.status_code == 201

    def test_valid_saves_on_db(self, _payload, session_maker):
        assert session_maker().query(models.Order).count() == 0
        response = client.post(self.build_url(), json=_payload)
        assert response.ok
        assert session_maker().query(models.Order).count() == 1

        order = session_maker().query(models.Order).first()
        assert response.json() == {
            'id': order.id,
            'user': order.user,
            'item': order.item,
            'is_active': order.is_active,
            'created_at': order.created_at.isoformat(),
        }

    def test_empity_returns_unprocessable_entity(self):
        response = client.post(self.build_url(), json={})
        assert response.status_code == 422

    def test_with_invalid_user_id_returns_404(self, _payload):
        _payload['user_id'] = 999
        response = client.post(self.build_url(), json=_payload)
        assert response.status_code == 404
        assert response.json() == {'detail': 'User does not exist.'}

    def test_with_invalid_item_id_returns_404(self, _payload):
        _payload['item_id'] = 999
        response = client.post(self.build_url(), json=_payload)
        assert response.status_code == 404
        assert response.json() == {'detail': 'Item does not exist.'}


@pytest.fixture
def order_fixture(_create_fake_user_and_item, session_maker):
    session = session_maker()

    order = models.Order(
        user=_create_fake_user_and_item.user.id,
        item=_create_fake_user_and_item.item.id,
    )
    session.add(order)
    session.flush()
    session.commit()

    info = collections.namedtuple('info', 'order session')
    return info(order=order, session=session)


@pytest.mark.usefixtures('use_db')
class TestDetailOrder:
    def build_url(self, _id):
        return f'{URL}/order/{_id}'

    def test_valid_returns_200(self, order_fixture):
        request = client.get(self.build_url(order_fixture.order.id))
        assert request.status_code == 200

    def test_valid_returns_complete_body(self, order_fixture):
        request = client.get(self.build_url(order_fixture.order.id))
        assert request.json() == {
            'id': order_fixture.order.id,
            'user': order_fixture.order.user,
            'item': order_fixture.order.item,
            'is_active': order_fixture.order.is_active,
            'created_at': order_fixture.order.created_at.isoformat(),
        }

    def test_unexist_email_returns_404(self):
        request = client.get(self.build_url('fakeOrderId'))
        assert request.status_code == 404
        assert request.json() == {'detail': 'Order does not exist.'}

    def test_valid_is_same_info_on_db(self, order_fixture, session_maker):
        request = client.get(self.build_url(order_fixture.order.id))
        order = session_maker().query(models.Order).first()
        assert request.json() == {
            'id': order.id,
            'user': order.user,
            'item': order.item,
            'is_active': order.is_active,
            'created_at': order.created_at.isoformat(),
        }
