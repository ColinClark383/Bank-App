from models.customer import Customer


class CustomerRepository:

    def __init__(self):
        self.customers = []
        self.next_id = 1

    def get_all(self):
        return self.customers

    def get_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def get_by_name(self, name):
        return [
            customer
            for customer in self.customers
            if name.lower() in customer.name.lower()
        ]

    def create(self, customer):
        self.customers.append(customer)

    def delete(self, customer):
        self.customers.remove(customer)