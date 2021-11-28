from app.api.customer.customer_data import CustomerData
from fastapi import FastAPI, status
from config.config import settings
import logging
import logging.config
import yaml
import os
import time
from app.infraestructure.database import db
from app.domain.customer.customer_model import Customer

logger = logging.getLogger(__name__)

def create_app():
    __set_timezone()
    __config_enviroments(settings.log_config_path)
    app = FastAPI()

    db.init_app(app)

    return app


def __config_enviroments(config_file_path):
    logging.getLogger().setLevel(settings.LOG_LEVEL)

    with open(config_file_path, 'rt') as config_file:
        config = yaml.safe_load(config_file.read())
        logging.config.dictConfig(config)


def __set_timezone():
    os.environ['TZ'] = 'America/Sao_Paulo'
    time.tzset()


app = create_app()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/customers", status_code=status.HTTP_201_CREATED)
async def create(customerData: CustomerData):
    # breakpoint()
    customer = await Customer.create(
        corporate_name=customerData.corporate_name,
        phone=customerData.phone,
        revenue=customerData.revenue)
    return customer.to_dict()


@app.get("/customers/{customer_id}", status_code=status.HTTP_200_OK)
async def show(customer_id: int):
    customer = await Customer.get_or_404(customer_id)
    return customer.to_dict()


@app.put("/customers/{customer_id}", status_code=status.HTTP_201_CREATED)
async def update(customer_id: int, customerData: CustomerData):
    customer = await Customer.get_or_404(customer_id)

    customer.update(**customerData.dict()).apply()
    return customer.to_dict()


@app.delete("/customers/{customer_id}", status_code=status.HTTP_200_OK)
async def destroy(customer_id: int):
    customer = await Customer.get_or_404(customer_id)
    await customer.delete()
    return ""