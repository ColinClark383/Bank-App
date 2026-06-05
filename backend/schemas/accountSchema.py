from pydantic import BaseModel

class CreateAccountRequest(BaseModel):
    customer_id: str
    account_type: str
    balance: float


class UpdateAccountRequest(BaseModel):
    account_type: str
    balance: float

class BalanceChangeRequest(BaseModel):
    balance_change: float