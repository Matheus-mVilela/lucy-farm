import pytest

import base_test
from app import models


@pytest.mark.usefixtures('use_db')
class TestOrder(base_test.TestBase):
    def test_create(self, session_maker):
        session = session_maker()
        user = self.create_fake_user(session)
        items = self.create_fake_items(session)

        order = models.Order(user=user.id, items=items)
        assert 0 == session.query(models.Order).count()
        session.add(order)
        session.flush()
        session.commit()
        assert 1 == session.query(models.Order).count()
        assert order == session.query(models.Order).first()

    def test_create_with_multiple_items(self, session_maker):
        session = session_maker()
        user = self.create_fake_user(session)
        items = self.create_fake_items(session, _quantity=10)

        order = models.Order(user=user.id, items=items)
        assert 0 == session.query(models.Order).count()
        session.add(order)
        session.flush()
        session.commit()
        assert 1 == session.query(models.Order).count()

        order = session.query(models.Order).first()
        assert 10 == len(order.items)

    def test_update(self, session_maker):
        session = session_maker()

        order = self.create_fake_order(session)
        assert 1 == len(order.items)

        items = self.create_fake_items(session, _quantity=3)
        order.items = items
        order.is_active = False
        session.add(order)
        session.commit()

        updated_order = session.query(models.Order).first()
        assert 3 == len(updated_order.items)
        assert not updated_order.is_active

    def test_delete(self, session_maker):
        session = session_maker()
        order = self.create_fake_order(session)
        assert 1 == session.query(models.Order).count()

        session.delete(order)
        session.commit()

        assert 0 == session.query(models.Order).count()

    def test_detail_user(self, session_maker):
        session = session_maker()
        user = self.create_fake_user(session)
        items = self.create_fake_items(session)

        order = self.create_fake_order(session, user=user, items=items)
        assert user.id == order.user
        assert items == order.items
