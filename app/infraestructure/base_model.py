from app.infraestructure.database import db

class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {'schema': 'customer_manager'}
