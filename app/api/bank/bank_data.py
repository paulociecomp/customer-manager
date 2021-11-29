from pydantic import BaseModel

class BankData(BaseModel):
    agency: str
    account: str
    bank_code: str