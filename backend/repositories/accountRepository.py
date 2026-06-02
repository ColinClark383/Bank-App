class AccountRepository:

    def __init__(self):
        self.accounts = []
        self.next_id = 1

    def get_all(self):
        return self.accounts

    def get_by_id(self, account_id):
        for account in self.accounts:
            if account.id == account_id:
                return account
        return None

    def get_by_customer_id(self, customer_id):
        return [
            account
            for account in self.accounts
            if account.customer_id == customer_id
        ]

    def create(self, account):
        self.accounts.append(account)

    def delete(self, account):
        self.accounts.remove(account)