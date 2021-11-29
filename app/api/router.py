from fastapi import FastAPI

from app.api.customer import customer_routers
from app.api.bank import bank_routers


def set_routes(app: FastAPI):
    app.include_router(customer_routers.router, tags=["Customers"])
    app.include_router(bank_routers.router, tags=["Banks"])
