from services.customerService import CustomerService
from repositories.customerRepository import CustomerRepository


def test_create_customer():

    repository = CustomerRepository()
    service = CustomerService(repository)

    customer = service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    assert customer.name == "Joe Smith"
    assert customer.email == "joe@email.com"


def test_get_customer():

    repository = CustomerRepository()
    service = CustomerService(repository)

    created = service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    customer = service.get_customer(created.id)

    assert customer is not None
    assert customer._id == created._id


def test_get_missing_customer():

    repository = CustomerRepository()
    service = CustomerService(repository)

    customer = service.get_customer(999)

    assert customer is None


def test_get_all_customers():

    repository = CustomerRepository()
    service = CustomerService(repository)

    service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    service.create_customer(
        "Bob Jones",
        "bob@email.com"
    )

    customers = service.get_all_customers()

    assert len(customers) == 2


def test_search_customers():

    repository = CustomerRepository()
    service = CustomerService(repository)

    service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    service.create_customer(
        "Bob Jones",
        "bob@email.com"
    )

    results = service.search_customers("Joe Smith")

    assert len(results) == 1
    assert results[0].name == "Joe Smith"


def test_update_customer():

    repository = CustomerRepository()
    service = CustomerService(repository)

    customer = service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    updated = service.update_customer(
        customer.id,
        "Joseph Smith",
        "joseph@email.com"
    )

    assert updated.name == "Joseph Smith"
    assert updated.email == "joseph@email.com"


def test_update_missing_customer():

    repository = CustomerRepository()
    service = CustomerService(repository)

    updated = service.update_customer(
        999,
        "Test",
        "test@email.com"
    )

    assert updated is None


def test_delete_customer():

    repository = CustomerRepository()
    service = CustomerService(repository)

    customer = service.create_customer(
        "Joe Smith",
        "joe@email.com"
    )

    success = service.delete_customer(
        customer.id
    )

    assert success is True
    assert service.get_customer(customer.id) is None


def test_delete_missing_customer():

    repository = CustomerRepository()
    service = CustomerService(repository)

    success = service.delete_customer(999)

    assert success is False