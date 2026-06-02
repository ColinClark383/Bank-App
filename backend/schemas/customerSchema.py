from pydantic import BaseModel


class CreateCustomerRequest(BaseModel):
    name: str
    email: str


class UpdateCustomerRequest(BaseModel):
    name: str
    email: str