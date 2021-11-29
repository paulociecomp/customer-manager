from dynaconf import settings
from gino.ext.starlette import Gino
from os import getenv

DATABASE_URL = getenv('DATABASE') if getenv('ENV_FOR_DYNACONF')  == 'production' else settings.DATABASE.URI

db = Gino(dsn=DATABASE_URL, schema=settings.DATABASE.SCHEMA)
