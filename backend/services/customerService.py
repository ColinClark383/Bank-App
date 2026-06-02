from models.customer import Customer


class CustomerService:

    def __init__(self, repository):
        self.repository = repository

    def get_all_customers(self):
        return self.repository.get_all()

    def get_customer(self, customer_id):
        return self.repository.get_by_id(customer_id)

    def search_customers(self, name):
        return self.repository.get_by_name(name)
    
    def get_premium_customers(self):
        return self.repository.get_premium()

    def create_customer(self, name, email):

        customer = Customer(
            id=self.repository.next_id,
            name=name,
            email=email
        )

        self.repository.next_id += 1

        self.repository.create(customer)

        return customer

    def update_customer(
        self,
        customer_id,
        name,
        email
    ):

        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            return None

        customer.name = name
        customer.email = email

        return customer

    def delete_customer(self, customer_id):

        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            return False

        self.repository.delete(customer)

        return True