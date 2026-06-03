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
    request: CreateAccountRequest
):

    account = accountService.create_account(
        request.customer_id,
        request.account_type,
        request.balance
    )

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return account

@router.get("/search")
def get_customer_accounts(
    id : str
):
    account = accountService.get_accounts_for_customer(id)
    
    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    
    return account

@router.put("/{account_id}")
def update_account(
    account_id: str,
    request: UpdateAccountRequest
):
    account = accountService.update_account(
        account_id,
        request.account_type,
        request.balance
    )

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return account

@router.get("")
def get_accounts():

    return accountService.get_all_accounts()

@router.get("/{account_id}")
def get_account(
    account_id: str
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
    account_id: str
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