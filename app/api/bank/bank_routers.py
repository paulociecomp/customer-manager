from app.domain.bank.bank_model import Bank
from app.domain.customer.customer_model import Customer
from fastapi import status, APIRouter
from app.api.bank.bank_data import BankData

router = APIRouter()

@router.post("/customers/{customer_id}/banks", status_code=status.HTTP_201_CREATED, response_model=BankData)
async def create(customer_id: int, bankData: BankData):
    customer = await Customer.get_or_404(customer_id)
    bank = await Bank.create(customer_id=customer.id, **bankData.dict())
    return BankData(**bank.to_dict())


@router.get("/customers/{customer_id}/banks/{bank_id}", status_code=status.HTTP_200_OK, response_model=BankData)
async def show(customer_id: int, bank_id: int):
    bank = await Bank.get_by(customer_id, bank_id)
    return BankData(**bank.to_dict())


@router.put("/customers/{customer_id}/banks/{bank_id}", status_code=status.HTTP_201_CREATED, response_model=BankData)
async def create(customer_id: int, bank_id: int, bankData: BankData):
    bank = await Bank.get_by(customer_id, bank_id)
    await bank.update(**bankData.dict()).apply()
    return BankData(**bank.to_dict())


@router.delete("/customers/{customer_id}/banks/{bank_id}", status_code=status.HTTP_200_OK)
async def show(customer_id: int, bank_id: int):
    bank = await Bank.get_by(customer_id, bank_id)
    await bank.delete()
    return ''

