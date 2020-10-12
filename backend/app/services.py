""" Services

This module is reponsible to handle all interactions to the database
"""

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
