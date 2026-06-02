from models.account import Account


class AccountService:

    def __init__(
        self,
        account_repository,
        customer_repository
    ):
        self.account_repository = account_repository
        self.customer_repository = customer_repository

    def create_account(
        self,
        customer_id,
        account_type,
        balance
    ):

        customer = self.customer_repository.get_by_id(
            customer_id
        )

        if customer is None:
            return None

        account = Account(
            id=self.account_repository.next_id,
            account_type=account_type,
            balance=balance,
            customer_id=customer_id
        )

        self.account_repository.next_id += 1

        self.account_repository.create(account)

        customer.accounts.append(account)

        return account
    
    def get_all_accounts(self):
        return self.account_repository.get_all()

    def get_accounts_for_customer(
        self,
        customer_name
    ):
        return self.customer_repository.get_by_name(
            customer_name
        )
    
    def get_account(
        self,
        account_id
    ):
        return self.account_repository.get_by_id(
            account_id
        )
    
    def update_account(
        self,
        account_id,
        account_type,
        balance
    ):
        account = self.account_repository.get_by_id(
            account_id
        )

        if account is None:
            return None

        account.account_type = account_type
        account.balance = balance

        return account
    
    def delete_account(
        self,
        account_id
    ):

        account = self.account_repository.get_by_id(
            account_id
        )

        if account is None:
            return False

        customer = self.customer_repository.get_by_id(
            account.customer_id
        )

        if customer:
            customer.accounts.remove(account)

        self.account_repository.delete(account)

        return True