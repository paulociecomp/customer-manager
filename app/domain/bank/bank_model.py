from app.domain.customer.customer_model import Customer
from app.infraestructure.base_model import BaseModel
from app.infraestructure.database import db
from app.domain.customer.customer_model import Customer

class Bank(BaseModel):
    __tablename__ = 'banks'

    id = db.Column(db.BigInteger(), primary_key=True)
    agency = db.Column(db.String, nullable=False)
    account = db.Column(db.String, nullable=False)
    bank_code = db.Column(db.String, nullable=False)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey(
            Customer.id),
        nullable=False)


    def get_by(customer_id, bank_id):
        return Bank.query.where(Bank.id == bank_id).where(Bank.customer_id == customer_id).gino.one()