""" Services

This module is reponsible to handle all interactions to the database
"""

import sqlalchemy.orm
from . import models, schemas


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
    user = db.query(models.User).get(email)
    if not user:
        if raise_error:
            raise DoesNotExisit('User does not exist')
        return None

    return user


def create_user(
    db: sqlalchemy.orm.Session,
    user: schemas.User,
    password: bool = None,
    persist: bool = True,
) -> models.User:

    _user = get_user_by_email(db, email=user.email)

    if _user and _user.hashed_password:
        raise ValidationError('Entity already exist')

    _user = _user or models.User()
    _user.username = user.username
    _user.email = user.email

    if password:
        # TODO: user_set_password()
        pass

    db.add(_user)
    if persist:
        db.commit()

    db.flush()
    return _user
