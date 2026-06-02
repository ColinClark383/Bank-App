from pydantic import BaseModel


class CreateAccountRequest(BaseModel):
    customer_id: int
    account_type: str
    balance: float


class UpdateAccountRequest(BaseModel):
    account_type: str
    balance: float