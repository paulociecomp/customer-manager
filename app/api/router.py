from fastapi import FastAPI

from app.api.customer import customer_routers


def set_routes(app: FastAPI):
    app.include_router(customer_routers.router, tags=["Customers"])
