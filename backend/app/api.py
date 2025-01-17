import typing

import fastapi
import sqlalchemy.orm

from . import database, models, schemas, services

# Create DB
models.Base.metadata.create_all(bind=database.engine)

_VERSION = '/api/v.1'
_SESSION_KEY = 'api_key'

app = fastapi.FastAPI(
    openapi_url=_VERSION + '/openapi.json', docs_url=_VERSION + '/docs',
)


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.exception_handler(services.ServicesException)
def handle_services_error(
    request: fastapi.Request, exception: services.ServicesException
):
    # TODO:
    # if isinstance(exception, services.APIKeyNotFound):
    #     return fastapi.responses.JSONResponse(status_code=403)

    if isinstance(exception, services.ValidationError):
        return fastapi.responses.JSONResponse(
            status_code=400, content={'detail': str(exception)}
        )

    if isinstance(exception, services.DoesNotExisit):
        return fastapi.responses.JSONResponse(
            status_code=404, content={'detail': str(exception)}
        )

    raise exception


@app.post(_VERSION + '/user', status_code=201, response_model=schemas.User)
def create_user(
    user: schemas.UserCreate,
    db: sqlalchemy.orm.Session = fastapi.Depends(get_db),
):
    return services.create_user(
        db=db, user=schemas.User(**user.dict()), password=user.password,
    )


@app.get(
    _VERSION + '/user/{email}', status_code=200, response_model=schemas.User
)
def read_user(
    email: str, db: sqlalchemy.orm.Session = fastapi.Depends(get_db),
):
    return services.get_user_by_email(db=db, email=email, raise_error=True)


@app.post(_VERSION + '/item', status_code=201, response_model=schemas.Item)
def create_item(
    item: schemas.Item, db: sqlalchemy.orm.Session = fastapi.Depends(get_db),
):
    return services.create_item(db=db, item=schemas.Item(**item.dict()))


@app.get(
    _VERSION + '/item/{name}', status_code=200, response_model=schemas.Item
)
def read_item(
    name: str, db: sqlalchemy.orm.Session = fastapi.Depends(get_db),
):
    return services.get_item_by_name(db=db, name=name, raise_error=True)


@app.get(
    _VERSION + '/items',
    status_code=200,
    response_model=typing.List[schemas.Item],
)
def list_item(db: sqlalchemy.orm.Session = fastapi.Depends(get_db)):
    return services.list_items(db=db)


@app.post(_VERSION + '/order', status_code=201, response_model=schemas.Order)
def create_order(
    order: schemas.OrderCreate,
    db: sqlalchemy.orm.Session = fastapi.Depends(get_db),
):
    return services.create_order(
        db=db, order=schemas.OrderCreate(**order.dict())
    )


@app.get(
    _VERSION + '/order/{_id}', status_code=200, response_model=schemas.Order
)
def read_order(
    _id: str, db: sqlalchemy.orm.Session = fastapi.Depends(get_db),
):
    return services.get_order_by_id(db=db, _id=_id, raise_error=True)


# TODO: create update Order endpoint and tests
