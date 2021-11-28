from dynaconf import settings
from gino.ext.starlette import Gino


db = Gino(dsn=settings.DATABASE.URI, schema=settings.DATABASE.SCHEMA)
