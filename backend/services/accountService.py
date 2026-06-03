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
            _id=None,
            customer_id=customer_id,
            account_type=account_type,
            balance=balance
        )

        return self.account_repository.create(
            account
        )

    def get_all_accounts(self):

        return self.account_repository.get_all()

    def get_accounts_for_customer(
        self,
        customer_id
    ):

        return self.account_repository.get_by_customer_id(
            customer_id
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

        self.account_repository.update(
            account
        )

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

        self.account_repository.delete(
            account
        )

        return True