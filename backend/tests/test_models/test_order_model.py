import pytest

import base_test
from app import models


@pytest.mark.usefixtures('use_db')
class TestOrder(base_test.TestBase):
    def test_create(self, session_maker):
        session = session_maker()
        assert 0 == session.query(models.Order).count()

        user = self.create_fake_user(session)
        order = models.Order(user_id=user.id)
        session.add(order)
        session.commit()
        assert 1 == session.query(models.Order).count()
        assert order == session.query(models.Order).first()

    def test_create_with_multiple_items(self, session_maker):
        session = session_maker()
        user = self.create_fake_user(session)
        items = self.create_fake_items(session, _quantity=10)

        assert 0 == session.query(models.Order).count()
        order = models.Order(user_id=user.id)
        session.add(order)
        session.commit()

        order = session.query(models.Order).first()
        order_item = self.create_fake_order_item(
            session, order=order, items=items
        )
        session.add(order)
        session.commit()
        assert 1 == session.query(models.Order).count()
        assert order == session.query(models.Order).first()

        assert 10 == len(items)
        assert 10 == len(order.items)
        for item, order_item in zip(items, order.items):
            assert item.id == int(order_item.item_id)

    def test_update(self, session_maker):
        session = session_maker()

        user = self.create_fake_user(session)
        order = self.create_fake_order(session, user=user)
        assert 1 == len(order.items)

        items = self.create_fake_items(session, _quantity=5)
        self.create_fake_order_item(session, order=order, items=items)
        order.is_active = False
        session.add(order)
        session.commit()

        updated_order = session.query(models.Order).first()
        assert 6 == len(updated_order.items)
        assert not updated_order.is_active

    def test_delete(self, session_maker):
        session = session_maker()

        user = self.create_fake_user(session)
        order = self.create_fake_order(session, user=user)
        assert 1 == session.query(models.Order).count()

        session.delete(order)
        session.commit()
        assert 0 == session.query(models.Order).count()

    def test_detail(self, session_maker):
        session = session_maker()

        user = self.create_fake_user(session)
        order = self.create_fake_order(session, user=user, create_items=False)

        items = self.create_fake_items(session, _quantity=5)
        order_item = self.create_fake_order_item(
            session, order=order, items=items
        )

        assert user.id == order.user_id
        for item, order_item in zip(items, order.items):
            assert item.id == int(order_item.item_id)
