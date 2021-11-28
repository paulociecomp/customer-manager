from fastapi import status, APIRouter
from app.domain.customer.customer_model import Customer
from app.api.customer.customer_data import CustomerData

router = APIRouter()


@router.post("/customers", status_code=status.HTTP_201_CREATED, response_model=CustomerData)
async def create(customerData: CustomerData):
    customer = await Customer.create(**customerData.dict())
    return CustomerData(**customer.to_dict())


@router.get("/customers/{customer_id}", status_code=status.HTTP_200_OK, response_model=CustomerData)
async def show(customer_id: int):
    customer = await Customer.get_or_404(customer_id)
    return CustomerData(**customer.to_dict())


@router.put("/customers/{customer_id}", status_code=status.HTTP_201_CREATED, response_model=CustomerData)
async def update(customer_id: int, customerData: CustomerData):
    customer = await Customer.get_or_404(customer_id)

    customer.update(**customerData.dict()).apply()
    return CustomerData(**customer.to_dict())


@router.delete("/customers/{customer_id}", status_code=status.HTTP_200_OK)
async def destroy(customer_id: int):
    customer = await Customer.get_or_404(customer_id)
    await customer.delete()
    return ""