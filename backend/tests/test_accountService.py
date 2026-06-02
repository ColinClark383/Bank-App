from services.accountService import AccountService
from services.customerService import CustomerService

from repositories.accountRepository import AccountRepository
from repositories.customerRepository import CustomerRepository


def create_services():

    customer_repository = CustomerRepository()
    account_repository = AccountRepository()

    customer_service = CustomerService(
        customer_repository
    )

    account_service = AccountService(
        account_repository,
        customer_repository
    )

    return (
        customer_service,
        account_service
    )

def test_create_account():

    customer_service, account_service = create_services()

    customer = customer_service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    account = account_service.create_account(
        customer.id,
        "checking",
        100
    )

    assert account.id == 1
    assert account.customer_id == customer.id
    assert account.balance == 100

def test_create_account_for_missing_customer():

    _, account_service = create_services()

    account = account_service.create_account(
        999,
        "checking",
        100
    )

    assert account is None

def test_get_account():

    customer_service, account_service = create_services()

    customer = customer_service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    created = account_service.create_account(
        customer.id,
        "checking",
        100
    )

    account = account_service.get_account(
        created.id
    )

    assert account.id == created.id

def test_get_missing_account():

    _, account_service = create_services()

    account = account_service.get_account(
        999
    )

    assert account is None

def test_get_all_accounts():

    customer_service, account_service = create_services()

    customer = customer_service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    account_service.create_account(
        customer.id,
        "checking",
        100
    )

    account_service.create_account(
        customer.id,
        "savings",
        200
    )

    accounts = account_service.get_all_accounts()

    assert len(accounts) == 2

def test_update_account():

    customer_service, account_service = create_services()

    customer = customer_service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    account = account_service.create_account(
        customer.id,
        "checking",
        100
    )

    updated = account_service.update_account(
        account.id,
        "savings",
        500
    )

    assert updated.account_type == "savings"
    assert updated.balance == 500

def test_update_missing_account():

    _, account_service = create_services()

    updated = account_service.update_account(
        999,
        "checking",
        100
    )

    assert updated is None

def test_delete_account():

    customer_service, account_service = create_services()

    customer = customer_service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    account = account_service.create_account(
        customer.id,
        "checking",
        100
    )

    success = account_service.delete_account(
        account.id
    )

    assert success is True
    assert account_service.get_account(account.id) is None

def test_delete_missing_account():

    _, account_service = create_services()

    success = account_service.delete_account(
        999
    )

    assert success is False