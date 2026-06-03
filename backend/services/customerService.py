from models.customer import Customer


class CustomerService:

    def __init__(self, repository, account):
        self.repository = repository
        self.account_repo = account

    def get_all_customers(self):
        return self.repository.get_all()

    def get_customer(self, customer_id):
        return self.repository.get_by_id(customer_id)

    def search_customers(self, name):
        return self.repository.get_by_name(name)
    
    def get_premium_customers(self):
        premium = []
        customers = self.get_all_customers()
        for customer in customers:
            total_value = 0
            accounts = self.account_repo.get_by_customer_id(customer._id)
            for account in accounts:
                total_value += account.balance

            if total_value >= 10000:
                premium.append(customer)

        return premium

    def create_customer(self, name, email):

        customer = Customer(
            name=name,
            email=email
        )

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

        self.repository.update(customer)

        return customer

    def delete_customer(self, customer_id):

        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            return False

        self.repository.delete(customer)

        return True