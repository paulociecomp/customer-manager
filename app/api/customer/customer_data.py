from pydantic import BaseModel


class CustomerData(BaseModel):
    corporate_name: str
    phone: str
    revenue: float
