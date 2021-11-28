from pydantic import BaseModel


class CustomerData(BaseModel):
    corporate_name: str
    phone: str
    revenue: float
    city: str
    postal_code: str
    state: str
    street: str
    number: str
    dstrict: str
    country: str
