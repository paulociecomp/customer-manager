
from app.infraestructure.base_model import BaseModel
from app.infraestructure.database import db
from datetime import datetime
from sqlalchemy import DateTime

class Customer(BaseModel):
    __tablename__ = "customers"

    id = db.Column(db.BigInteger(), primary_key=True)
    corporate_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    dstrict = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    created_at = db.Column("created_at", DateTime,
                         default=datetime.now,
                         onupdate=datetime.now,
                         nullable=False)
    updated_at = db.Column("updated_at", DateTime,
                         default=datetime.now,
                         onupdate=datetime.now,
                         nullable=False)
    revenue = db.Column(db.Float, nullable=False)
