from repositories.customerRepository import CustomerRepository
from repositories.accountRepository import AccountRepository

from services.customerService import CustomerService
from services.accountService import AccountService

customerRepository = CustomerRepository()
accountRepository = AccountRepository()

customerService = CustomerService(
    customerRepository,
    accountRepository
)

accountService = AccountService(
    accountRepository,
    customerRepository
)