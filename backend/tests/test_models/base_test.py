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
        self, session, username=None, email=None, hashed_password=None
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
        session.flush()
        session.commit()
        return user

    def payload_item(self):
        return {
            'name': f'Leite-{uuid.uuid4()}',
            'price': round(random.uniform(1, 999), 2),
            'measure': str(uuid.uuid4()),
        }

    def create_fake_items(
        self, session, name=None, price=None, measure=None, _quantity=1
    ):
        payload_item = self.payload_item()
        if not name:
            name = payload_item['name']
        if not price:
            price = payload_item['price']
        if not measure:
            measure = payload_item['measure']

        items = []
        for _ in range(_quantity):
            if _quantity > 1:  # force random fields
                name = f'Leite-{uuid.uuid4()}'
                price = round(random.uniform(1, 999), 2)
                measure = str(uuid.uuid4())

            item = models.Item(name=name, price=price, measure=measure)
            items.append(item)
            session.add(item)

        session.flush()
        session.commit()
        return items

    def create_fake_order(self, session, user=None, items=None):
        if not user:
            user = self.create_fake_user(session)
        if not items:
            items = self.create_fake_items(session)

        order = models.Order(user=user.id, items=items)

        session.add(order)
        session.flush()
        session.commit()
        return order
