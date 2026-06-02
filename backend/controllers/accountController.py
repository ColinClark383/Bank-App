from fastapi import APIRouter, HTTPException

from datastore import accountService

from schemas.accountSchema import (
    CreateAccountRequest,
    UpdateAccountRequest
)

router = APIRouter(
    prefix="/api/accounts"
)

@router.post("")
def create_account(
    customer_id: int,
    request: CreateAccountRequest
):

    account = accountService.create_account(
        customer_id,
        request.account_type,
        request.balance
    )

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return account

@router.get("")
def get_accounts(customer_id: int):

    return accountService.get_accounts_for_customer(
        customer_id
    )

@router.get("/{account_id}")
def get_account(
    customer_id: int,
    account_id: int
):
    account = accountService.get_account(
        account_id
    )

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return account

@router.delete("/{account_id}")
def delete_account(
    customer_id: int,
    account_id: int
):

    success = accountService.delete_account(
        account_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return {
        "message": "Account deleted"
    }