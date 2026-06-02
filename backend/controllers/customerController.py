from fastapi import APIRouter, HTTPException
from datastore import customerService
from schemas.customerSchema import (
    CreateCustomerRequest,
    UpdateCustomerRequest
)

router = APIRouter(prefix="/api/customers")

@router.get("")
def get_all_customers():
    return customerService.get_all_customers()


@router.get("/premium")
def get_premium_customers():
    return customerService.get_premium_customers()

@router.get("/search")
def search_customer(name: str):
    return customerService.search_customers(name)

@router.get("/{customer_id}")
def get_customer(customer_id: int):

    customer = customerService.get_customer(customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer

@router.post("", status_code=201)
def create_customer(request: CreateCustomerRequest):

    return customerService.create_customer(
        request.name,
        request.email
    )

@router.put("/{customer_id}")
def update_customer(
    customer_id: int,
    request: UpdateCustomerRequest
):

    customer = customerService.update_customer(
        customer_id,
        request.name,
        request.email
    )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int):

    success = customerService.delete_customer(customer_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {"message": "Customer deleted"}
