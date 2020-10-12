import pytest

from app import models


@pytest.mark.usefixtures("use_db")
class TestItem:
    @pytest.fixture
    def _create_fake_item(self, payload_item, session_maker):
        session = session_maker()

        item = models.Item(
            name=payload_item["name"],
            price=payload_item["price"],
            measure=payload_item["measure"],
        )

        session.add(item)
        session.flush()
        session.commit()

        return (item, session)

    def test_create(self, payload_item, session_maker):
        session = session_maker()

        item = models.Item(
            name=payload_item["name"],
            price=payload_item["price"],
            measure=payload_item["measure"],
        )

        assert 0 == session.query(models.Item).count()

        session.add(item)
        session.flush()
        session.commit()

        assert 1 == session.query(models.Item).count()
        assert item == session.query(models.Item).first()

    def test_delete(self, _create_fake_item):
        item, session = _create_fake_item
        assert 1 == session.query(models.Item).count()

        session.delete(item)
        session.commit()

        assert 0 == session.query(models.Item).count()
