""" Services

This module is reponsible to handle all interactions to the database
"""

import typing

# import hashlib
# import secrets

import sqlalchemy.orm

from . import models, schemas, security


class ServicesException(Exception):
    """ Data Access Exception
    This error is raised when data passed to the function is not valid
    """

    pass


class ValidationError(ServicesException):
    pass


class DoesNotExisit(ServicesException):
    pass


# --- User --- #
def get_user_by_id(
    db: sqlalchemy.orm.Session, _id: str, raise_error: bool = False,
) -> models.User:
    user = db.query(models.User).filter(models.User.id == _id).first()

    if not user:
        if raise_error:
            raise DoesNotExisit('User does not exist.')
        return None

    return user


def get_user_by_email(
    db: sqlalchemy.orm.Session, email: str, raise_error: bool = False,
) -> models.User:
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        if raise_error:
            raise DoesNotExisit('User does not exist.')
        return None

    return user


def create_user(
    db: sqlalchemy.orm.Session,
    user: schemas.User,
    password: str = None,
    persist: bool = True,
) -> models.User:

    if not password:
        raise ValidationError('Password is empty.')

    _user = get_user_by_email(db, email=user.email)
    if _user and _user.hashed_password:
        raise ValidationError('User already exist.')

    _user = _user or models.User()
    _user.username = user.username
    _user.email = user.email
    _user.hashed_password = security.get_password_hash(password)

    db.add(_user)
    if persist:
        db.commit()

    db.flush()
    return _user


# --- Item --- #
def get_item_by_id(
    db: sqlalchemy.orm.Session, _id: str, raise_error: bool = False
) -> models.Item:
    item = db.query(models.Item).filter(models.Item.id == _id).first()

    if not item:
        if raise_error:
            raise DoesNotExisit('Item does not exist.')
        return None

    return item


def get_item_by_name(
    db: sqlalchemy.orm.Session, name: str, raise_error: bool = False
) -> models.Item:
    item = db.query(models.Item).filter(models.Item.name == name).first()

    if not item:
        if raise_error:
            raise DoesNotExisit('Item does not exist.')
        return None

    return item


def create_item(
    db: sqlalchemy.orm.Session, item: schemas.Item, persist: bool = True
) -> models.Item:
    _item = get_item_by_name(db, name=item.name)
    if _item:
        raise ValidationError('Item already exist.')

    _item = _item or models.Item()
    _item.name = item.name
    _item.price = item.price
    _item.measure = item.measure

    db.add(_item)
    if persist:
        db.commit()

    db.flush()
    return _item


def list_items(db: sqlalchemy.orm.Session) -> typing.List[models.Item]:
    return db.query(models.Item).all()


# --- Order --- #
def get_order_by_id(
    db: sqlalchemy.orm.Session, _id: str, raise_error: bool = False
) -> models.Order:

    order = db.query(models.Order).get(_id)
    if not order:
        if raise_error:
            raise DoesNotExisit('Order does not exist.')
        return None

    return order


def create_order(
    db: sqlalchemy.orm.Session,
    order: schemas.OrderCreate,
    persist: bool = True,
) -> models.Order:

    user = get_user_by_id(db, _id=order.user_id, raise_error=True)
    item = get_item_by_id(db, _id=order.item_id, raise_error=True)

    order = models.Order(user=user.id, item=item.id)
    db.add(order)
    if persist:
        db.commit()

    db.flush()
    return order
