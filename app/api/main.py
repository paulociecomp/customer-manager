from fastapi import FastAPI
from config.config import settings
import logging
import logging.config
import yaml
import os
import time
from app.infraestructure.database import db
from app.api.router import set_routes

logger = logging.getLogger(__name__)

def create_app():
    __set_timezone()
    __config_enviroments(settings.log_config_path)
    app = FastAPI()

    db.init_app(app)
    set_routes(app)

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
