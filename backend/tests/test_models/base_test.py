import random
import uuid

from app import models


class TestBase:
    def payload_user(self):
        return {
            'username': 'Rick',
            'email': 'wubbaLubbaDubDub@sanchez.com',
            'hashed_password': str(uuid.uuid4()),
        }

    def create_fake_user(
        self,
        session,
        username=None,
        email=None,
        hashed_password=None,
        commit=True,
    ):
        payload_user = self.payload_user()
        if not username:
            username = payload_user['username']
        if not email:
            email = payload_user['email']
        if not hashed_password:
            hashed_password = payload_user['hashed_password']

        user = models.User(
            username=username, email=email, hashed_password=hashed_password,
        )
        session.add(user)
        if commit:
            session.flush()
            session.commit()
        return user

    def payload_item(self):
        return {
            'name': f'Leite-{uuid.uuid4()}',
            'measure': str(uuid.uuid4()),
        }

    def create_fake_items(
        self, session, name=None, measure=None, commit=True, _quantity=1
    ):
        payload_item = self.payload_item()
        if not name:
            name = payload_item['name']
        if not measure:
            measure = payload_item['measure']

        items = []
        for _ in range(_quantity):
            if _quantity > 1:  # force random fields
                name = f'Leite-{uuid.uuid4()}'
                measure = str(uuid.uuid4())

            item = models.Item(name=name, measure=measure)
            items.append(item)
            session.add(item)

        if commit:
            session.flush()
            session.commit()
        return items

    def create_fake_order_item(
        self, session, order=None, items=None, commit=True
    ):
        if not order:
            order = self.create_fake_order(session)
        if not items:
            items = self.create_fake_items(session)

        order_items = []
        for item in items:
            order_item = models.OrderItem(
                order_id=order.id,
                item_id=item.id,
                price=round(random.uniform(20, 100), 2),
                discount=round(random.uniform(0, 20), 2),
            )
            order_items.append(order_item)
            session.add(order_item)

        if commit:
            session.flush()
            session.commit()
        return order_items

    def create_fake_order(self, session, user=None, create_items=True):
        if not user:
            user = self.create_fake_user(session)

        order = models.Order(user_id=user.id)
        session.add(order)
        session.commit()

        if create_items:
            order_item = self.create_fake_order_item(session, order=order)
            order.items = order_item

        session.add(order)
        session.commit()
        return order
