import pytest

from app import models


@pytest.mark.usefixtures('use_db')
class TestUser:
    @pytest.fixture
    def _create_fake_user(self, payload, session_maker):
        session = session_maker()

        user = models.User(
            username=payload['username'],
            email=payload['email'],
            hashed_password=payload['hashed_password'],
        )
        session.add(user)
        session.flush()
        session.commit()

        return (user, session)

    def test_create(self, payload, session_maker):
        session = session_maker()

        user = models.User(
            username=payload['username'],
            email=payload['email'],
            hashed_password=payload['hashed_password'],
        )

        assert 0 == session.query(models.User).count()

        session.add(user)
        session.flush()
        session.commit()

        assert 1 == session.query(models.User).count()
        assert user == session.query(models.User).first()

    def test_update(self, _create_fake_user):
        user, session = _create_fake_user

        user.username = 'UpdatedName'
        user.email = 'UpdatedEmail'
        user.hashed_password = 'UpdatedHashedPassword'

        session.add(user)
        session.commit()

        updated_user = session.query(models.User).first()
        assert updated_user.username == 'UpdatedName'
        assert updated_user.email == 'UpdatedEmail'
        assert updated_user.hashed_password == 'UpdatedHashedPassword'

    def test_delete(self, _create_fake_user):
        user, session = _create_fake_user
        assert 1 == session.query(models.User).count()

        session.delete(user)
        session.commit()

        assert 0 == session.query(models.User).count()

    def test_detail(self, payload, _create_fake_user):
        user, session = _create_fake_user
        assert user.username == payload['username']
        assert user.email == payload['email']
        assert user.hashed_password == payload['hashed_password']
