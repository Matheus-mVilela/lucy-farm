import pytest

import base_test
from app import models


@pytest.mark.usefixtures('use_db')
class TestUser(base_test.TestBase):
    def test_create(self, session_maker):
        payload_user = self.payload_user()
        session = session_maker()

        user = models.User(
            username=payload_user['username'],
            email=payload_user['email'],
            hashed_password=payload_user['hashed_password'],
        )

        assert 0 == session.query(models.User).count()

        session.add(user)
        session.flush()
        session.commit()

        assert 1 == session.query(models.User).count()
        assert user == session.query(models.User).first()

    def test_update(self, session_maker):
        session = session_maker()
        user = self.create_fake_user(session)

        user.username = 'UpdatedName'
        user.email = 'UpdatedEmail'
        user.hashed_password = 'UpdatedHashedPassword'

        session.add(user)
        session.commit()

        updated_user = session.query(models.User).first()
        assert updated_user.username == 'UpdatedName'
        assert updated_user.email == 'UpdatedEmail'
        assert updated_user.hashed_password == 'UpdatedHashedPassword'

    def test_delete(self, session_maker):
        session = session_maker()
        user = self.create_fake_user(session)
        assert 1 == session.query(models.User).count()

        session.delete(user)
        session.commit()

        assert 0 == session.query(models.User).count()

    def test_detail(self, session_maker):
        session = session_maker()
        payload_user = self.payload_user()
        user = self.create_fake_user(
            session, hashed_password=payload_user['hashed_password']
        )
        assert user.username == payload_user['username']
        assert user.email == payload_user['email']
        assert user.hashed_password == payload_user['hashed_password']
